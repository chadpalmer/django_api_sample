let int_current_axiom = 0;

const toggle_axiom_id_box = () => {
    if (document.getElementById("choose").checked) {
        document.getElementById("choose_box").className = "choose_box show";
    } else {
        document.getElementById("choose_box").className = "choose_box";
    }
};

const validate_form = () => {
    let bln_valid = true;
    if (document.getElementById("choose").checked) {
        if (isNaN(parseInt(document.getElementById("axiom_id").value)) || parseInt(document.getElementById("axiom_id").value) < 1 || parseInt(document.getElementById("axiom_id").value) > num_axioms) {
            bln_valid = false;
        }
    }
    if (bln_valid) {
        toggle_error(false);
        build_api_url();
    } else {
        toggle_error(true);
    }
};

const toggle_error = (bln_error) => {
    if (bln_error) {
        document.getElementById("axiom_id").className = "axiom_id_box error";
        document.getElementById("error_box").className = "error_box show";
    } else {
        document.getElementById("axiom_id").className = "axiom_id_box";
        document.getElementById("error_box").className = "error_box";
    }
};

const get_random_number = (min, max) => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
};

const build_api_url = () => {
    let url = document.location;
    if (document.getElementById("choose").checked) {
        url += document.getElementById("axiom_id").value + "/";
    } else {
        let int_random_id = get_random_number(1, num_axioms);
        while (int_random_id === int_current_axiom) {
            int_random_id = get_random_number(1, num_axioms);
        }
        int_current_axiom = int_random_id;
        url += int_random_id.toString() + "/";
    }
    load_axiom(url);
};

const load_axiom = async (url) => {
    const response = await fetch(url);
    const json = await response.json();
    display_axiom(json);
};

const display_axiom = (json) => {
    document.getElementById("axiom_category").innerText = json.category;
    document.getElementById("axiom_text").innerText = json.text;
};

window.onload = () => {
    /* add click events to radio buttons */
    let axiom_radios = document.getElementsByName("axiom_choice");
    for (let i = 0; i < axiom_radios.length; i++) {
        axiom_radios[i].onclick = toggle_axiom_id_box;
    }

    /* add click event to axiom button */
    document.getElementById("get_axiom").onclick = validate_form;
};
