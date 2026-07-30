const claimInput =
    document.getElementById("claim");

const urlInput =
    document.getElementById("url");

const verifyButton =
    document.getElementById("verifyButton");

const status =
    document.getElementById("status");

const result =
    document.getElementById("result");

const verdict =
    document.getElementById("verdict");

const evidence =
    document.getElementById("evidence");


verifyButton.addEventListener("click", async () => {

    const claim =
        claimInput.value.trim();

    const url =
        urlInput.value.trim();


    if (!claim || !url) {

        status.textContent =
            "Please enter both a claim and a URL.";

        return;
    }


    verifyButton.disabled = true;

    status.textContent =
        "Preparing verification...";

    result.classList.add("hidden");


    try {

        /*
         * GenLayer contract integration
         * will be connected here.
         */

        await new Promise(
            resolve => setTimeout(resolve, 1000)
        );


        verdict.textContent =
            "UNCERTAIN";


        evidence.textContent =
            "Waiting for GenLayer contract integration.";


        result.classList.remove("hidden");


        status.textContent =
            "Verification interface ready.";

    }

    catch (error) {

        status.textContent =
            "Verification failed: " +
            error.message;

    }

    finally {

        verifyButton.disabled = false;

    }

});
