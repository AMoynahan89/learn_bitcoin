function toggleNav() {
  var navbar = document.getElementById("drop-down");
  if (navbar.classList.contains("open")) {
      navbar.classList.remove("open");
  } else {
      navbar.classList.add("open");
  }
}

// Create and display qr images
function handleDonationButton(event) {
  let dataAmount;

  if (event.target.classList.contains("make-qr")) {
    dataAmount = event.target.getAttribute("data-amount");
  } else if (event.target.id === "custom-donation") {
      dataAmount = document.getElementById("donation-amount").value;
      console.log("Donation Amount:", dataAmount);
  }
  
  fetch(`/make_qr?amount=${dataAmount}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById("qr-code").src = `data:image/png;base64,${data.img}`;
      document.getElementById("qr-code").style.display = "block";
    })
    .catch(error => console.error("Error:", error));
}

document.querySelectorAll(".make-qr").forEach(button => {
  button.addEventListener("click", handleDonationButton);
})

document.getElementById("custom-donation").addEventListener("click", handleDonationButton);



document.querySelectorAll(".block-nav-item").forEach(item => {
  item.addEventListener("click", function() {
      const height = this.dataset.height;
      fetch(`/load_block_data?height=${height}`)
          .then(response => response.json())
          .then(data => {
              document.getElementById("block-id").textContent = data.id;
              document.getElementById("block-merkle-root").textContent = data.merkle_root;
              document.getElementById("block-previousblockhash").textContent = data.previousblockhash;
              document.getElementById("block-height").textContent = data.height;
              document.getElementById("block-timestamp").textContent = data.timestamp;
              document.getElementById("block-nonce").textContent = data.nonce;
              document.getElementById("block-tx-count").textContent = data.tx_count;
              document.getElementById("block-version").textContent = data.version;
              document.getElementById("block-bits").textContent = data.bits;
              document.getElementById("block-difficulty").textContent = data.difficulty;
              document.getElementById("block-mediantime").textContent = data.mediantime;
              document.getElementById("block-reward").textContent = data.reward;
              document.getElementById("block-medianFee").textContent = data.medianFee;
              document.getElementById("block-totalFees").textContent = data.totalFees;
              document.getElementById("block-pool-name").textContent = data.pool_name;
              document.getElementById("block-weight").textContent = data.weight;
              document.getElementById("block-size").textContent = data.size;
          });
  });
});


