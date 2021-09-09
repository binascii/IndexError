import time

from oval_graph.arf_xml_parser.arf_xml_parser import ARFXMLParser

rule = 'xccdf_org.ssgproject.content_rule_enable_fips_mode'
src = 'tests/test_data/ssg-fedora-ds-arf.xml'

print("Benchmark xml to oval_tree")
print("Start process rule: ", rule)
print("report-xml: ", src)
start_time = time.time()

xml_parser = ARFXMLParser(src)
oval_tree = xml_parser.get_oval_tree(rule)

print("rule {} --- {} seconds ---".format(rule, time.time() - start_time))

print("Start process all rules")
print("report-xml: ", src)
start_time_all_rules = time.time()


xml_parser_all_rules = ARFXMLParser(src)

for rule in xml_parser_all_rules.used_rules:
    oval_tree = xml_parser_all_rules.get_oval_tree(rule)
print("{} rules --- {} seconds ---".format(
    len(xml_parser_all_rules.used_rules),
    time.time() - start_time_all_rules
))
