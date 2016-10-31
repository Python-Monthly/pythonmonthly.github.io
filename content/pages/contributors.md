Title: Contributors
Date: 2016-10-30


<div id="repositories">
  
</div>
<script>
$(document).ready(function() {
  var repoName = "";
  contributorName = "";
  $.getJSON("https://api.github.com/orgs/Python-Monthly/repos", function(repo) {
    $.each(repo, function(repoIndex, repoValue) {
      $("#repositories").append("<h2>* " + repoValue.name + "</h2>" + repoValue.description + "<br><br>");
      $.getJSON(repoValue.contributors_url, function(contributors) {
        $.each(contributors, function(contribIndex, contribValue) {
          $("#repositories").append("<img src='" + contribValue.avatar_url + "' height='80px' width='80px' style='margin:1px;float:left;'>");
          $("#repositories").append("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;");
          $("#repositories").append("<div><a href='" + contribValue.html_url + "'>" + contribValue.login + "</div></a><br><br>");
        });
      });
      
      
    });
    
  });
});
</script>
