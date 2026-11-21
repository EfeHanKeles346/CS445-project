from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree as E
from copy import deepcopy
import sys

source, target = map(Path, sys.argv[1:])
with ZipFile(source) as z:
    original = {n: z.read(n) for n in z.namelist()}
with ZipFile(target) as z:
    revised = {n: z.read(n) for n in z.namelist()}
c = 'http://schemas.openxmlformats.org/drawingml/2006/chart'
chart = 'ppt/slides/charts/chart1.xml'
old = E.fromstring(original[chart]); new = E.fromstring(revised[chart])
old_series = old.findall('.//{%s}ser' % c)
new_series = new.findall('.//{%s}ser' % c)
assert len(old_series) == len(new_series) == 1
for old_s, new_s in zip(old_series, new_series):
    for tag in ['tx', 'cat', 'val']:
        old_part = old_s.find('{%s}%s' % (c, tag))
        new_part = new_s.find('{%s}%s' % (c, tag))
        assert old_part is not None and new_part is not None
        new_s.replace(new_part, deepcopy(old_part))
for x in new.findall('{%s}externalData' % c): new.remove(x)
new.append(deepcopy(old.find('{%s}externalData' % c)))
revised[chart] = E.tostring(new, xml_declaration=True, encoding='UTF-8')
rel = 'ppt/slides/charts/_rels/chart1.xml.rels'
revised[rel] = original[rel]
for n, data in original.items():
    if n.startswith('ppt/embeddings/'):
        revised[n] = data
ct = 'http://schemas.openxmlformats.org/package/2006/content-types'
old_ct = E.fromstring(original['[Content_Types].xml'])
new_ct = E.fromstring(revised['[Content_Types].xml'])
for item in old_ct:
    if item.get('Extension') == 'xlsx' or 'embeddings/' in item.get('PartName', ''):
        if not any(dict(i.attrib) == dict(item.attrib) for i in new_ct):
            new_ct.append(deepcopy(item))
revised['[Content_Types].xml'] = E.tostring(new_ct, xml_declaration=True, encoding='UTF-8')
with ZipFile(target, 'w', ZIP_DEFLATED) as z:
    for n, data in revised.items(): z.writestr(n, data)
print('Preserved original chart workbook bytes and cell references')
