import sys
from datetime import datetime

TEMPLATE = """
Title: Project: {title}
Date: {year}-{month}-{day}
status: hidden
save_as: pages/projects/{title}.html

<div id="description"></div>
<div id="link"></div>

###Contributors to the project

<div id="contributors"></div>
<script>
$(document).ready(function() {{
  $.getJSON("https://api.github.com/repos/Python-Monthly/{title}", function(repo) {{ //get the repo data
    $("#link").append("<a href='" + repo.html_url + "'>Project link on Github</a>");
    $("#description").append(repo.description + "<br><br>"); //output the repo description
    $.getJSON(repo.contributors_url, function(contributors) {{ //get the contributors data
      $.each(contributors, function(contribIndex, contribValue) {{ //for each contributor output their avatar and username with link to their github profile
      $("#contributors").append("<img src='" + contribValue.avatar_url + "' height='90px' width='90px' style='margin:5px;float:left;'>");
      $("#contributors").append("&nbsp;");
      $("#contributors").append("<br><a href='" + contribValue.html_url + "'>" + contribValue.login + "</a><br><br><br>");
      }});
    }});
  }});
}});
</script>
"""


def make_entry(title):
    today = datetime.today()
    f_create = "content/pages/projects/{}.md".format(title)
    t = TEMPLATE.strip().format(title=title.title(),
                                year=today.year,
                                month=today.month,
                                day=today.day)

    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print("No project name provided")

