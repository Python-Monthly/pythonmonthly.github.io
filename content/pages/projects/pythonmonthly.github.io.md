Title: Project: pythonmonthly.github.io
Date: 2016-11-3
status: hidden
save_as: pages/projects/pythonmonthly.github.io.html

<div id="description"></div>
<div id="link"></div>

###Contributors to the project

<div id="contributors"></div>
<script>
$(document).ready(function() {
  $.getJSON("https://api.github.com/repos/Python-Monthly/pythonmonthly.github.io", function(repo) { //get the repo data
    $("#link").append("<a href='" + repo.html_url + "'>Project link on Github</a>");
    $("#description").append(repo.description + "<br><br>"); //output the repo description
    $.getJSON(repo.contributors_url, function(contributors) { //get the contributors data
      $.each(contributors, function(contribIndex, contribValue) { //for each contributor output their avatar and username with link to their github profile
      $("#contributors").append("<img src='" + contribValue.avatar_url + "' height='90px' width='90px' style='margin:5px;float:left;'>");
      $("#contributors").append("&nbsp;");
      $("#contributors").append("<br><a href='" + contribValue.html_url + "'>" + contribValue.login + "</a><br><br><br>");
      });
    });
  });
});
</script>
