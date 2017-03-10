Title: Projects
Date: 10-31-2016

Below is a list of all projects by the Python Monthly group. You may click on the link for a description of the project as well as the contributors to that project.

<div id="repositories">

</div>

<script>
$(document).ready(function() {
  $.getJSON("https://api.github.com/orgs/Python-Monthly/repos", function(repo) {
    $.each(repo, function(repoIndex, repoValue) {
      $("#repositories").append(repoIndex+1 + ". <a href='projects/" + repoValue.name + ".html'>" + repoValue.name + "</a><br>");
      
      
      
    });
    
  });
});
</script>
