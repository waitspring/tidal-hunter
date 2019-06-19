/*
 * my javascript functions for tidal-hunter project
 */

function deploy_notice(statement) {
    alert(statement);
}


function deploy_output(title, uri) {
    layer.open(
        {
            type: 2,
            title: title,
            area: ["800px", "800px"],
            shadeClose: true,
            content: uri
        }
    );
}