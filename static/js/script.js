async function getDataJson(url, elmntId, query) {
  const apiCall = await fetch(url);
  console.log(apiCall)
  const response = await apiCall.json();
  console.log(response)
  document.getElementById(elmntId).innerHTML = response[query];
  console.log(response[query])
}

async function getDataValue(url, elmntId) {
  const apiCall = await fetch(url);
  console.log(apiCall)
  const response = await apiCall.text();
  console.log(response)
  document.getElementById(elmntId).innerHTML = response;
}


