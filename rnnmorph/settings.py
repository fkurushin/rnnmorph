import os
from collections import defaultdict
try:
    from importlib.resources import files
    MODELS_FOLDER = str(files(__name__) / "models")
except ImportError:
    # Fallback for Python < 3.9
    from importlib_resources import files
    MODELS_FOLDER = str(files(__name__) / "models")
LANGUAGES = ("ru", "en")

FILES = dict()
FILES["build_config"] = "build_config.json"
FILES["train_config"] = "train_config.json"
FILES["train_model_config"] = "train_model.json"
FILES["train_model_weights"] = "train_model.h5"
FILES["eval_model_config"] = "eval_model.json"
FILES["eval_model_weights"] = "eval_model.h5"
FILES["gram_input"] = "gram_input.json"
FILES["gram_output"] = "gram_output.json"
FILES["word_vocabulary"] = "word_vocabulary.pickle"
FILES["char_set"] = "char_set.txt"
FILES["char_model_config"] = "char_model.json"
FILES["char_model_weights"] = "char_model.h5"

MODELS_PATHS = defaultdict(dict)
for language in LANGUAGES:
    for key, file_name in FILES.items():
        MODELS_PATHS[language][key] = os.path.join(MODELS_FOLDER, language, file_name)

TEST_TAGGED_FOLDER = str(files(__name__) / "test" / "tagged")
TEST_UNTAGGED_VK = str(files(__name__) / "test" / "untagged" / "VK_extracted.txt")
TEST_UNTAGGED_LENTA = str(files(__name__) / "test" / "untagged" / "Lenta_extracted.txt")
TEST_UNTAGGED_JZ = str(files(__name__) / "test" / "untagged" / "JZ_extracted.txt")
TEST_TAGGED_VK = str(files(__name__) / "test" / "tagged" / "VK_extracted.txt")
TEST_TAGGED_LENTA = str(files(__name__) / "test" / "tagged" / "Lenta_extracted.txt")
TEST_TAGGED_JZ = str(files(__name__) / "test" / "tagged" / "JZ_extracted.txt")
TEST_TAGGED_EN_EWT_UD = str(files(__name__) / "test" / "tagged" / "en_ewt_ud_extracted.txt")
TEST_GOLD_VK = str(files(__name__) / "test" / "gold" / "VK_gold.txt")
TEST_GOLD_LENTA = str(files(__name__) / "test" / "gold" / "Lenta_gold.txt")
TEST_GOLD_JZ = str(files(__name__) / "test" / "gold" / "JZ_gold.txt")
TEST_GOLD_EN_EWT_UD = str(files(__name__) / "test" / "gold" / "en_ewt_ud_test.txt")
