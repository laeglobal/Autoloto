import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from data_scraping.scrape_lottery_data import scrape_ny_lottery


def test_scrape_lottery_results():
    # Ejecutar el script de scraping
    scrape_ny_lottery()

    # Verificar que el archivo CSV se haya creado
    assert os.path.exists('data/ny_lottery_results.csv')

    # Verificar que el archivo no esté vacío
    assert os.path.getsize('data/ny_lottery_results.csv') > 0
