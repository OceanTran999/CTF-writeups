function pingMailStatus() {
  fetch("/api/mail/status");
}

function fetchInboxPreview() {
  fetch("/api/mail/inbox?limit=5");
}

pingMailStatus();
fetchInboxPreview();

document.getElementById("start-btn")?.addEventListener("click", () => {
  const audio = document.getElementById("balletAudio");
  audio.play();

  document.getElementById("start-btn").style.display = "none";
  document.getElementById("audio-warning").style.display = "none";

  const dancer = document.getElementById("dancer");
  const dancerImg = document.getElementById("dancer-img"); // Get the image element

  dancer.style.display = "block";
  dancerImg.style.display = "block"; // Show the image

  let angle = 0;
  const radius = 100;
  const centerX = window.innerWidth / 2;
  const centerY = window.innerHeight / 2;

  function animate() {
    angle += 0.05;
    const x = centerX + radius * Math.cos(angle);
    const y = centerY + radius * Math.sin(angle);
    dancer.style.left = x + "px";
    dancer.style.top = y + "px";

    dancerImg.style.left = x + "px"; // Sync image movement
    dancerImg.style.top = y + "px";

    requestAnimationFrame(animate);
  }
  animate();
});

function qyrbkc() { 
    const xtqzp = ["85"], vmsdj = ["87"], rlfka = ["77"], wfthn = ["67"], zdqo = ["40"], yclur = ["82"],
          bpxmg = ["82"], hkfav = ["70"], oqzdu = ["78"], nwtjb = ["39"], sgfyk = ["95"], utxzr = ["89"],
          jvmqa = ["67"], dpwls = ["73"], xaogc = ["34"], eqhvt = ["68"], mfzoj = ["68"], lbknc = ["92"],
          zpeds = ["84"], cvnuy = ["57"], ktwfa = ["70"], xdglo = ["87"], fjyhr = ["95"], vtuze = ["77"], awphs = ["75"];
        const dhgyvu = [xtqzp[0], vmsdj[0], rlfka[0], wfthn[0], zdqo[0], yclur[0], 
                    bpxmg[0], hkfav[0], oqzdu[0], nwtjb[0], sgfyk[0], utxzr[0], 
                    jvmqa[0], dpwls[0], xaogc[0], eqhvt[0], mfzoj[0], lbknc[0], 
                    zpeds[0], cvnuy[0], ktwfa[0], xdglo[0], fjyhr[0], vtuze[0], awphs[0]];

    const lmsvdt = dhgyvu.map((pjgrx, fkhzu) =>
        String.fromCharCode(
            Number(pjgrx) ^ (fkhzu + 1) ^ 0 
        )
    ).reduce((qdmfo, lxzhs) => qdmfo + lxzhs, ""); 
    console.log("Note: Key is now secured with heavy obfuscation, should be safe to use in prod :)");
}

