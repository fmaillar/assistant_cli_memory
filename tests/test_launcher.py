import os
import sys

# Allow importing from repository root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entrypoints.launcher import slugify


def test_slugify_with_accents_and_punctuation():
    assert slugify('Éléphant rose!') == 'elephant_rose'


def test_slugify_collapses_multiple_separators():
    assert slugify('Hello---World!!  example') == 'hello_world_example'
