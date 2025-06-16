import numpy as np
import matplotlib.pyplot as plt

def plot_sample(data, label='Stichprobe'):
    """
    Zeichnet die Werte einer Stichprobe mit Mittelwertlinie.
    
    Parameter:
    - data: 1D-arrayartige Stichprobe
    - label: Beschriftung der Stichprobe (für Legende)
    - farbe: Farbe der Linie/Punkte
    """
    data = np.array(data)
    mean = np.mean(data)
    
    plt.plot(data, 'o-', color="blue", linestyle='None', label=label)
    plt.axhline(mean, color="red", linestyle='--', label=f'{label} (Mittelwert = {mean:.2f})')

def plot_box(samples, labels=None, title='Boxplot mehrerer Gruppen'):
    """
    Erstellt Boxplots für eine Liste von Stichproben.

    Parameter:
    - samples: Liste von 1D-Arrays oder Listen mit den Stichprobenwerten
    - labels: Beschriftungen der Gruppen (Liste von Strings)
    - title: Titel des Plots
    """
    plt.figure(figsize=(6, 5))

    # Boxplot zeichnen
    plt.boxplot(samples, showmeans=True)

    # Achsenbeschriftung
    n = len(samples)
    if labels is None:
        labels = [f'Gruppe {i+1}' for i in range(n)]
    plt.xticks(range(1, n + 1), labels)

    plt.ylabel('Wert')
    plt.title(title)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

def plot_violin(samples, labels=None, title='Violinplot mit Datenpunkten & Medianbeschriftung', jitter_strength=0.05):
    """
    Violinplots mit sichtbaren Datenpunkten und Beschriftung der Mediane.
    
    Parameter:
    - samples: Liste von Arrays oder Listen mit Stichprobenwerten
    - labels: Bezeichnungen der Gruppen (Liste von Strings)
    - title: Titel des Plots
    - jitter_strength: Stärke der horizontalen Streuung der Punkte
    """
    plt.figure(figsize=(6, 5))
    n = len(samples)
    positions = range(1, n + 1)

    # Violinplot
    plt.violinplot(samples, positions=positions, showmeans=True, showmedians=True)

    for i, data in enumerate(samples):
        data = np.array(data)
        x_pos = positions[i]
        
        # Punkte mit Jitter
        jitter = np.random.normal(loc=0, scale=jitter_strength, size=len(data))
        plt.scatter(x_pos + jitter, data, color='black', alpha=0.6, s=10)

        # Median berechnen und beschriften
        median = np.median(data)
        plt.text(x_pos + 0.15, median, f'Median: {median:.2f}', va='center', fontsize=9, color='darkred')

    # Achsen und Layout
    if labels is None:
        labels = [f'Gruppe {i+1}' for i in range(n)]
    plt.xticks(positions, labels)
    plt.ylabel('Wert')
    plt.title(title)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()