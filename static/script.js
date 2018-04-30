let btn = document.getElementById('check');
let input = document.getElementById('input');
let output = document.getElementById('output');

btn.addEventListener('click', function() {

    let httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState != 4) return;
        let wormholes = JSON.parse(httpRequest.responseText);
        let world_sigs = input.value.split('\n').map(s => s.split('\t')[0].substr(0, 3));
        let scout_sigs = wormholes.map(x => x.signatureId);
        let comp_array = [];
        for (let sig of world_sigs) {
            if (!scout_sigs.includes(sig)) {
                comp_array.push([true, sig]);
            }
        }
        for (let sig of scout_sigs) {
            if (!world_sigs.includes(sig)) {
                comp_array.push([false, sig]);
            }
        }
        comp_array = comp_array.sort((a, b) => {
            if (a[1] < b[1]) return -1;
            if (a[1] > b[1]) return 1;
            return 0;
        });
        output.textContent = comp_array.map(x => (x[0] ? '+' : '-') + x[1]).join('\n');
    };
    httpRequest.open('GET', '/wormholes', true);
    httpRequest.send(null);
});