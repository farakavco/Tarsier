<%inherit file="mail_master.mak" />

<table width="600" cellpadding="0" cellspacing="0" border="0" align="center" style="background-color:#fff;border-radius:3px;border:1px solid #e5e5e5;">
    <tr>
        <td>
            <table width="900" cellpadding="15" cellspacing="0" border="0" align="center">
                <tbody>
                <!-- spacing -->
                <tr>
                    <td width="100%" height="0"></td>
                </tr>
                <!-- start of author avatar -->
                <tr>
                    <td align="center">
                        <a target="_blank" href="${author.html_url}" title="${author.username}">
                            <img class="avatar" width="110" height="110" style="display:block; border-radius: 50%; outline:none; text-decoration:none;" src="${author.avatar_url}">
                        </a>
                    </td>
                </tr>
                <!-- Title -->
                <tr>
                    <td style="font-family:Tahoma, sans-serif; font-size: 16px; font-weight:bold; color: #c10e0e; text-align:center;line-height: 24px;">
                       ${title}
                    </td>
                </tr>
                <!-- content -->
                <tr>
                    <td style="font-family:Tahoma, sans-serif; font-size: 14px; font-weight:bold; color: #333333; text-align:left;line-height: 24px;">
                        <p style="font-size:14px"><b>Today:</b></p>
                        <ul>
                            %for commit in commits:
                                 <li style="font-size:12px">
                                     <span style="font-size:14px; color: #8a8a8a;">[${commit.repo}]:</span>
                                     ${commit.message}
                                 </li>
                            %endfor
                        </ul>
                        <p style="font-size:14px">
                            <b>Tomorrow:</b>
                        </p>
                        <br>
                        <p style="font-size:14px">
                            <b>Blocking:</b>
                        </p>
                    </td>
                </tr>
                </tbody>
            </table>
        </td>
    </tr>
</table>
