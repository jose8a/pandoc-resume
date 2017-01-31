import json

JSONRESUME = "../.info/pandoc-resume.json"
MDRESUME = "../.info/resume-general.md"

jsonresume = open(JSONRESUME)
md_resume = open(MDRESUME, 'w')

jsondata = json.load(jsonresume)


def md_generate_contact(data):
    md_resume.write(data['name'] + "\n")


def md_generate_value(data):
    md_resume.write("\n")
    md_resume.write("# Value" + "\n")
    for i in range(len(data)):
        md_resume.write("  * " + data[i] + "\n")


def md_generate_skills(data):
    md_resume.write("\n")
    md_resume.write("# Skills" + "\n")
    for i in range(len(data)):
        md_resume.write("  * " + data[i] + "\n")


def md_generate_history(data):
    md_resume.write("\n")
    md_resume.write("# Experience" + "\n")
    for item in range(len(data)):
        md_resume.write("\n")
        md_resume.write(data[item]['employer'] + "\n")
        md_resume.write(data[item]['title'] + "\n")
        md_resume.write(data[item]['location'] + "\n")
        md_resume.write(data[item]['dates'] + "\n")
        md_resume.write(data[item]['description'] + "\n")


def md_generate_schools(data):
    md_resume.write("\n")
    md_resume.write("# Schools" + "\n")
    for i in range(len(data)):
        md_resume.write("\n")
        md_resume.write(data[i]['name'] + "\n")
        md_resume.write(data[i]['location'] + "\n")
        md_resume.write(data[i]['degree'] + "\n")
        md_resume.write(data[i]['dates'] + "\n")


md_generate_contact(jsondata['contact'])
md_generate_value(jsondata['valueprop'])
md_generate_skills(jsondata['skills'])
md_generate_history(jsondata['history'])
md_generate_schools(jsondata['schools'])

print("Closing markdown-resume file.")
md_resume.close()
