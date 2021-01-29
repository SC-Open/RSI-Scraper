import pytest
from .validator import assert_valid_schema

@pytest.mark.starmap
def test_request_systems():
	from rsi_scrapper import StarmapSystems

	object = StarmapSystems('pyro')
	data = object.execute()
	assert data is not None

	assert_valid_schema(data, 'starmap_systems.json')

@pytest.mark.starmap
def test_request_search():
	from rsi_scrapper import StarmapSearch

	object = StarmapSearch('Stanton')
	data = object.execute()
	assert data is not None

	assert_valid_schema(data, 'starmap_search.json')

@pytest.mark.starmap
def test_request_object():
	from rsi_scrapper import StarmapCelestialObjects

	object = StarmapCelestialObjects('TOHIL.PLANETS.TOHILIII')
	data = object.execute()
	assert data is not None

	assert_valid_schema(data, 'starmap_object.json')

@pytest.mark.starmap
def test_request_star_system():
	from rsi_scrapper import StarmapStarSystems

	object = StarmapStarSystems('STANTON')
	data = object.execute()
	assert data is not None

	assert_valid_schema(data, 'starmap_star_system.json')

@pytest.mark.starmap
def test_request_tunnels():
	from rsi_scrapper import StarmapTunnels

	object = StarmapTunnels('1188')
	data = object.execute()
	assert data is not None

	assert_valid_schema(data, 'starmap_tunnels.json')

@pytest.mark.starmap
def test_request_species():
	from rsi_scrapper import StarmapSpecies

	object = StarmapSpecies()
	data = object.execute()
	assert data is not None

	assert_valid_schema(data, 'starmap_species.json')