import pytest
import requests

from ..helpers import api_helper, mock


def test_wikimedia_API_runs():
    req = requests.get("https://fr.wikipedia.org/w/api.php")
    assert req.status_code == 200

def test_wikimedia_return_page_id(monkeypatch):
    results = {
        "query": {
                "search": [
                    {
                        "pageid": 681159,
                    }
                ]
            }
        }

    def mockreturn(request, params):
        # I use the library 'requests-mock' to mock a Requests' response.
        return mock.mock_requests(results)

    monkeypatch.setattr(requests, 'get', mockreturn)

    assert api_helper.ApiHelper._get_wikipedia_page_id("Paris") == 681159

def test_wikimedia_return_text(monkeypatch):
    results = {
        "query": {
            "search": [
                {
                    "pageid": 681159,
                }
            ],
            "pages": [
                {
                    "extract": "<p><b>Paris</b> (prononcé <span title=\"Alphabet phonétique international\">[<span title=\"[p] « p » dans « papa »\">p</span><span title=\"[a] « a » dans « patte »\">a</span><span title=\"[.] indique la séparation entre deux syllabes\">.</span><span title=\"[ʁ] « r » dans « roue »\">ʁ</span><span title=\"[i] « i » dans « si »\">i</span>]</span> ) est la capitale de la France. Elle se situe au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré, le bassin parisien, sur une boucle de la Seine, entre les confluents de celle-ci avec la Marne et l'Oise. Ses habitants s’appellent les Parisiens. Paris est également le chef-lieu de la région Île-de-France et l'unique commune française qui est en même temps un département. Commune centrale de la métropole du Grand Paris, créée en 2016, elle est divisée en arrondissements, comme les villes de Lyon et de Marseille, au nombre de vingt. L’État y dispose de prérogatives particulières exercées par le préfet de police de Paris.</p>\n<p>Ville la plus peuplée de France, elle est quatrième parmi les aires urbaines européennes derrière Moscou, Istanbul et Londres et la <abbr class=\"abbr\" title=\"Vingt-neuvième\">29<sup>e</sup></abbr> plus peuplée du monde. Paris compte 2,21 millions d'habitants au <time class=\"nowrap\" datetime=\"2015-01-01\" data-sort-value=\"2015-01-01\"><abbr class=\"abbr\" title=\"premier\">1<sup>er</sup></abbr> janvier 2015</time>. L'agglomération parisienne s’est largement développée au cours du <abbr class=\"abbr\" title=\"20ᵉ siècle\"><span>XX</span><sup style=\"font-size:72%\">e</sup></abbr> siècle, rassemblant 10,71 millions d'habitants au <time class=\"nowrap\" datetime=\"2015-01-01\" data-sort-value=\"2015-01-01\"><abbr class=\"abbr\" title=\"premier\">1<sup>er</sup></abbr> janvier 2015</time>, et son aire urbaine (l'agglomération et la couronne périurbaine) comptait 12,53 millions d'habitants.</p>\n"
                }
            ]
            }
        }

    def mockreturn(request, params):
        # I use the library 'requests-mock' to mock a Requests' response.
        return mock.mock_requests(results)

    monkeypatch.setattr(requests, 'get', mockreturn)

    assert api_helper.ApiHelper.get_wikipedia_result("Paris") == "Paris (prononcé [pa.ʁi] ) est la capitale de la France. Elle se situe au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré, le bassin parisien, sur une boucle de la Seine, entre les confluents de celle-ci avec la Marne et l'Oise. Ses habitants s’appellent les Parisiens. Paris est également le chef-lieu de la région Île-de-France et l'unique commune française qui est en même temps un département. Commune centrale de la métropole du Grand Paris, créée en 2016, elle est divisée en arrondissements, comme les villes de Lyon et de Marseille, au nombre de vingt. L’État y dispose de prérogatives particulières exercées par le préfet de police de Paris."
