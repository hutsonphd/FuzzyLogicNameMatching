$(document).ready(function() {
	$('#mappings').DataTable({
		dom:'<"d-flex justify-content-between"l<"d-flex justify-content-between-3"fB>>tip',
		buttons: [
			{
				extend:'csv',
				className: 'btn btn-secondary ms-4'
			},
			{
				extend:'print',
				className: 'btn btn-secondary mx-1'
			}
		]
	});
} );