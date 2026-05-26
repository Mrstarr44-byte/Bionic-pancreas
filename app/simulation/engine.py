class SimulationEngine:

    BG_MIN = 20.0
    BG_MAX = 600.0
    CARB_FACTOR = 4.0
    INSULIN_FACTOR = 40.0

    @staticmethod
    def calculate_new_bg(current_bg, carbs=0.0, insulin=0.0):
        new_bg = current_bg + (carbs * SimulationEngine.CARB_FACTOR) - (insulin * SimulationEngine.INSULIN_FACTOR)
        new_bg = round(new_bg, 1)

        # Güvenlik sınırları (tıbbi limitler)
        if new_bg < SimulationEngine.BG_MIN:
            new_bg = SimulationEngine.BG_MIN
        elif new_bg > SimulationEngine.BG_MAX:
            new_bg = SimulationEngine.BG_MAX

        # Durum belirleme
        if new_bg < 70:
            status = "hypoglycemia"
        elif new_bg <= 180:
            status = "normal"
        else:
            status = "hyperglycemia"

        return {"new_bg": new_bg, "status": status}
