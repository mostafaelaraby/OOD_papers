

from utils import generate_md_file
import bibtexparser
import os

file_name = str(os.path.join(os.getcwd(),'bibtex.bib'))

with open(file_name) as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_db = bibtexparser.loads(bibtex_str, parser=bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False))

################################### Create Readme ####################################
def plot_titles(titles):
    return '\n' + "## " + titles[0] + '\n'

list_types = [["Classics", "Classic"],
               ["Empirical Study", "Empirical", "Theoretical"],
               ["Surveys", "Survey", "survey", "review"],
               ["Adversarial Attack Detection", "Adversarial"],
               ["Uncertainty-based Methods", "dropout", "ensemble", "uncertainty"],
               ['Generative-based Methods', 'GAN', 'auto-encoder', 'vae', 'diffusion', 'synthesis'],
               ["Novelty Discovery", "Novel"],
               ["Regularization Methods", "Regularization"],
               ["Gradient-based Methods", "gradients", "gradient"],
               ["Output-based Methods", "post-hoc", "output", "outlier exposure", "postprocess"],
               ["Label Space Redesign" , "label"],
               ["Bayesian Models", "bayes"],
               ["Density-based Methods", "gaussian", "dirac", "density", "poisson"],
               ["Distance-based Methods", "distance" ], 
               ["Distillation-based Methods", "transfer", "teacher" ], 
               ["Preprocessing-based Methods", "preprocessor"],
               ["Miscellaneous", "Misc"], 
               ["Libraries", "Library", "Software"],
               ["Workshops", 'Workshop']]

generate_md_file(DB=bib_db, list_classif=list_types, key="keywords", plot_title_fct=plot_titles, filename= "README.md", add_comments=True)


