const form = document.getElementById("review-form");

form.addEventListener("submit", function (event) {
  event.preventDefault(); // empêche le rechargement de la page

  // Récupérer les données
  const comment = document.getElementById("comment").value;

  const rating = document.querySelector('input[name="rating"]:checked');

  if (!rating) {
    alert("Please select a rating ⭐");
    return;
  }

  alert("Review submitted ! 🎉\nRating: " + rating.value + "\nComment: " + comment);

  // Optionnel : reset du formulaire
  form.reset();
});