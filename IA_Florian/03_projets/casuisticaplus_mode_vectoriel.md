## CasuisticaPlus – Modèle vectoriel pondéré

### 🔹 Introduction

Dans le système IA_Florian, le discernement des situations complexes repose sur un cadre à 12 dimensions représentant les axes de l’identité active. Afin de comparer des cas, des états ou des intentions, une formalisation vectorielle a été adoptée. Cette approche permet de modéliser chaque situation comme un **vecteur dans un espace pondéré**, et d’évaluer la proximité entre deux états via l’**angle entre ces vecteurs**.

### 🔹 Cadre mathématique

#### Définition des vecteurs

Chaque situation est représentée comme un vecteur :

\[
\vec{u} = (u_1, u_2, ..., u_{12})
\]

Chaque composante \( u_i \) correspond à une intensité ou un impact sur l’une des 12 dimensions :

1. Technique  
2. Organisationnelle  
3. Documentaire  
4. Automatisation  
5. Stratégique  
6. Personnel  
7. Cognitif  
8. Intérieur  
9. Spirituel  
10. Rayonnement  
11. Stylistique  
12. Capitalisation

#### Pondération

Chaque axe est affecté d’un poids \( w_i \), permettant de prioriser certaines dimensions selon le contexte (ex : poids fort sur Spirituel et Intérieur pour les cas vocationnels).

#### Formule du cos(θ) pondéré

\[
\cos(\theta) = \frac{\sum_{i=1}^{12} w_i \cdot u_i \cdot v_i}{\sqrt{\sum_{i=1}^{12} w_i \cdot u_i^2} \cdot \sqrt{\sum_{i=1}^{12} w_i \cdot v_i^2}}
\]

- \( \vec{u} \), \( \vec{v} \) : vecteurs représentant deux états ou situations  
- \( w_i \) : pondération de la dimension \( i \)  
- \( \theta \) : angle entre les vecteurs

### 🔹 Interprétation

- **cos(θ) ≈ 1** : états très proches, convergence d’intention ou de structure
- **cos(θ) ≈ 0** : indépendance, orthogonalité des dimensions (aucune compatibilité)
- **cos(θ) < 0** : opposition marquée, incohérence stratégique ou morale

Ce coefficient permet une mesure **qualitative de la proximité directionnelle**, indépendamment des amplitudes absolues.

### 🔹 Application dans IA_Florian

Chaque cas est vectorisé par analyse pondérée, manuelle ou semi-automatique (via des heuristiques, annotations ou scripts Python). Les cas archivés dans `05_cas_concrets/` possèdent un champ vectoriel associé. L’assistant IA évalue automatiquement le cos(θ) avec les états de référence :

- Situation idéale (alignement souhaité)
- Situation réelle actuelle
- Situation redoutée

Cette triangulation permet d’orienter la décision vers le **plus faible écart angulaire** avec l’idéal, tout en détectant les oppositions structurelles avec les états à éviter.

### 🔹 Références

- Paul Ricoeur, *Soi-même comme un autre*, 1990 – sur la dynamique de l’ipséité et la tension entre identité narrative et éthique.
- Saint Ignace de Loyola, *Exercices spirituels* – sur le discernement des esprits et la pesée intérieure des motions.
- Mikolov et al., *Efficient Estimation of Word Representations in Vector Space*, 2013 – pour l’usage de cos(θ) dans les espaces vectoriels sémantiques.
- François Jullien, *Figures de l’immanence* – pour la pensée en tension au lieu d’une dialectique de l’opposition.

### 🔹 Limites

- Ne capture pas la dynamique temporelle (un même cos(θ) peut avoir des conséquences très différentes selon le moment).
- La pondération est arbitraire si non fondée sur un discernement explicite.
- La linéarité de l’espace vectoriel ne rend pas compte des non-linéarités du réel (effets seuils, ruptures).

---

Ce fichier est une référence canonique pour toute analyse vectorielle au sein du système IA_Florian.

