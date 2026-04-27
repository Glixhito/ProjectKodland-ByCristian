import random

class Memory:
    def __init__(self):
        self.history = []
        self.corruption_level = 0

    def store(self, question, answer):
        self.history.append({
            "question": question,
            "answer": answer,
            "original_answer": answer,
            "corrupted": False
        })

    def corrupt(self):
        if not self.history:
            return

        self.corruption_level += 0.05
        chance = min(0.15 + self.corruption_level * 0.1, 0.6)

        if random.random() < chance:
            entry = random.choice(self.history)
            entry["corrupted"] = True
            entry["answer"] = random.choice([
                "[Registro alterado]",
                "Eso no fue lo que dijiste.",
                "Respuesta inconsistente."
            ])

        # recuperación mínima
        for entry in self.history:
            if entry["corrupted"] and random.random() < 0.05:
                entry["answer"] = entry["original_answer"]
                entry["corrupted"] = False

    def recall(self):
        if not self.history:
            return None

        entry = random.choice(self.history)

        if entry["corrupted"] and random.random() < 0.5:
            return None

        return entry["question"], entry["answer"]
