### FILES:
* contact.json:
* social.json:
* work-history.json:
* schools.json
* elearning.json
* skills.json:
* projects.json

# Tools
  - pandoc
  - mactex (or any other LaTex tool that works with pandoc)
  - json2yaml (via npm)

# Overview
We start with individual sections of a typical resume (contact-info, experience, skills, etc) broken out into JSON data files.  These are combined and converted into a YAML file that the Pandoc tool can consume and parse as a data file for its templates.  Then we use the Pandoc tool (which relies on a LaTex tool - e.g. MacTex) to convert the pandoc template into a PDF file.

# Process
1a. Inputs: start with the module *.json files
1b. Inputs: start with a template.tex file for the final output format

2. IntermediateFile: merge the *.json files into a single resume.json file
2b. Use a simple python script to merge them:

```
    $> json-resume-merge.py
```

3a. IntermediateFile: converte the resume.json file into resume.yaml file using the json2yaml utility (install via npm)

```
    $> json2yaml resume.json resume.yaml
```


3b. Add `---` to beginning of resume.yaml as Pandoc requires that to parse as data file
3c. Add `...` to end of resume.yaml as Pandoc requires this as well

4. Outputs:

```
  $> pandoc --template="resume-template.tex" resume.yaml -o resume.pdf
```


