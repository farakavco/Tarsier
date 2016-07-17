<%inherit file="mail_master.mak" />

<div style="text-align: left">
    <a target="_blank" href="${author.html_url}" title="${author.username}" style="float: left;">
        <img class="avatar" width="50" height="50" style="display:block; border-radius: 50%; outline:none; text-decoration:none;" src="${author.avatar_url}">
    </a>
    <h1 style="font-size: 16px;margin: 0px 0 10px 60px;line-height: 25px;color: #505050;">${author.username}</h1>
    <h3 style="font-size: 12px;margin: 0;margin-left: 60px;color: #5789bf">${date}</h3>
</div>
<div style="margin-left: 25px;border-left: 2px solid #9632b7;padding-left: 0px;">
    <div style="height: 40px;"></div>
    <p style="font-size:12px;font-weight: bold;background: #9632b7;display: inline-block;padding: 3px 11px;color: #fff;border-bottom-right-radius: 3px;border-top-right-radius: 3px;">Today</p>
    <ul style="padding-left: 0px;margin: 0;">
        %for commit in commits:
             <li style="font-size:12px;list-style:none;margin-left:10px;font-weight:bold;line-height: 25px;">
                 <span style="font-size: 13px;color: #585858;font-weight: bold;margin-right: 7px;">${commit.repo} ⟶</span>
                 <a href="${commit.url}" style="font-size: 11px;font-family: monospace;border: 1px solid #335f98;padding: 3px 7px;background-color: #4078c0;color: #fff;font-weight: bold;border-radius: 3px;margin-right: 7px;">${commit.sha[:6]}</a>
                 ${commit.message}
             </li>
        %endfor
    </ul>
    <br>
    <p style="font-size:12px;list-style: none;margin:0;margin-left: 10px!important;line-height: 25px;">Did you do anymore???!!!</p>
    <br>
    <br>
    <p style="font-size:12px;font-weight: bold;background: #9632b7;display: inline-block;padding: 3px 11px;color: #fff;border-bottom-right-radius: 3px;border-top-right-radius: 3px;">Tomorrow</p>
    <p style="font-size:12px;list-style: none;margin:0;margin-left: 10px!important;line-height: 25px;">Empty space is so boring... go on be descriptive...</p>
    <br>
    <br>
    <p style="font-size:12px;font-weight: bold;background: #9632b7;display: inline-block;padding: 3px 11px;color: #fff;border-bottom-right-radius: 3px;border-top-right-radius: 3px;">Blocking</p>
    <p style="font-size:12px;list-style: none;margin:0;margin-left: 10px!important;line-height: 25px;">Empty space is so boring... go on be descriptive...</p>

</div>

