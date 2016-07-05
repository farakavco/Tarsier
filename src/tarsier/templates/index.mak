<%inherit file="local:templates.master"/>

<%def name="title()">
  Commit
</%def>
<div class="row">
    <div class="col-md-12">

        <div class="box">
            <form action="/" method="get">
                <label class="lable">Since Date: </label><input type="text" name="date" class="date  form-control"/>
                <button type="submit" class="btn btn-warning">Submit</button>
            </form>
        </div>

        <div class="jumbotron box">
            <h1 class="center-block text-center">Commits List</h1>
            %if items:
                %for item in items:
                    <article>
                        <header class="col-md-12 center-block padding-bottom">
                            <a href="${item.github_url}" title="${item.username}" class="avatar help-block col-md-2 center-block text-center">
                                <img src="${item.avatar}" class="img-circle help-block center-block">
                            </a>
                            <h3 class="col-md-12 center-block text-center username">${item.username}</h3>
                        </header>
                        <div class="col-md-12 commit-list">
                            %for key, val in item.commits.items():
                                <h3>${key}  <span class="smallest">( commits: ${len(val)} )</span></h3>
                                <ul class="commit-container col-md-12">
                                    %for v in val:
                                        <a href="${v.url}" title="${v.sha}" class="col-md-5 commit-box">
                                             <li>
                                                <p class="smaller text-sha"><b>Sha: </b> ${v.sha}</p>
                                                <p class="smallest">${v.time}</p>
                                                <p class="message smaller"><b>Message: </b>${v.message}</p>
                                            </li>
                                        </a>

                                    %endfor
                                  </ul>
                            %endfor
                        </div>
                    </article>
                %endfor
            %else:
                <p>There is no commit.</p>
            %endif
            <a class="btn btn-primary btn-lg opacity" href="http://www.turbogears.org" target="_blank">
            ${h.icon('book')} Learn more
            </a>
        </div>
    </div>
</div>
