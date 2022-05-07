const form = document.querySelector('#rnaForm');

form.addEventListener('submit', async e => {
    e.preventDefault();
    const rnaSeq = document.querySelector('#rnaSequence');
    const output = document.querySelector('#rnaFamily');

    if (!rnaSeq.value) {
        swal("Invalid", "RNA Sequence cannot be empty!", "error");
        return;
    }

    document.body.className = 'loading';
    output.value = "Loading     ";
    const loading = "  /:---:  \\:  |".split(":");
    let i = 0;
    const load = setInterval(() => {
        output.value = output.value.substring(0, output.value.length-2);
        output.value = output.value + loading[(i % loading.length)];
        i ++;
    }, 125);
    
    const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            rna: rnaSeq.value
        })
    });

    const rna = await response.json();
    if (rna.family) {
        clearInterval(load);
        document.body.className = '';
    }
    output.value = rna.family;
})