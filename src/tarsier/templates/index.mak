<%inherit file="local:templates.master"/>

<%def name="title()">
</%def>
<div class="row">
    <div class="col-md-12">

        <div class="box">
            <form action="/" method="get">
                <label class="lable">Start Date: </label>
                <input id="start_date" type="text"  class="start-date date  form-control"/>
                <input id="start_date_mask" type="text" name="start_date" class="date hidden form-control"/>
                <label class="lable">End Date: </label>
                <input id="end_date" type="text"  class="end-date date  form-control"/>
                <input id="end_date_mask" type="text" name="end_date" class="date hidden form-control"/>
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
                            %if item.has_commit is False:
                                <p class="no-commit">This user has no commit in this range date.</p>
                            %else:
                                %for repo, commit in item.commits.items():
                                    %if commit:
                                        <h3> ${repo} <span class="smallest">( commits: ${len(commit)})</span></h3>
                                        <ul class="commit-container col-md-12">
                                            %for v in commit:
                                                <a href="${v.url}" title="${v.sha}" class="col-md-5 commit-box">
                                                     <li>
                                                        <p class="smaller text-sha"><b>Sha: </b> ${v.sha}</p>
                                                        <p class="smallest">${v.time}</p>
                                                        <p class="message smaller"><b>Message: </b>${v.message}</p>
                                                    </li>
                                                </a>
                                            %endfor
                                        </ul>
                                    %endif
                                %endfor
                            %endif
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
