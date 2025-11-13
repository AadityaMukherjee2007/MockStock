// alert("script loaded");

document.getElementById("company_name").onchange = () => {
    const admin_auth = document.getElementById("admin_passwd");

    if (document.getElementById("company_name").value === "Admin") {
        admin_auth.style.display = "block";
    } else {
        admin_auth.style.display = "none";
    }
};

document.querySelector("form").onsubmit = (event) => {
    event.preventDefault();

    const company_name = document.getElementById("company_name").value;
    // alert(company_name);

    if (company_name === "Admin") {
        const admin_auth = document.getElementById("admin_passwd");
        const passwd = admin_auth.value;

        if (passwd === "biswayan89")
            window.location.href = "/admin_interface"; 
        else 
            window.alert("Wrong Password");
    } else {
        window.location.href = `/company_interface/${company_name}`; 
    }
};