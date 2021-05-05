var api;

function watch(link){
    var domain = "meet.jit.si";
    var options = {
        roomName: link,
        width: document.width,
        height: document.height,
        parentNode: undefined,
        configOverwrite: {},
        interfaceConfigOverwrite: {}
    }
    api = new JitsiMeetExternalAPI(domain, options);
}
