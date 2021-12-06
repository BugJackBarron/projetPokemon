 let advancedSearchPlus = document.getElementById('recherche_avancee');
 advancedSearchPlus.addEventListener('click',() => {
	 let advancedSearch = document.getElementById('advancedSearchForm');
	 if (advancedSearch.style.display == 'none') {
		advancedSearch.style.display = 'block';
		advancedSearchPlus.innerHTML="-";
	 }
	 else {
		 advancedSearch.style.display = 'none';
		 advancedSearchPlus.innerHTML="+";
	 }
	 
 });