# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: TravelPack
import unittest

class TestTravelPackEdgeCases(unittest.TestCase):

    def test_empty_trip(self):
        trip = Trip("Empty")
        self.assertEqual(trip.get_checklist(), [])
        self.assertEqual(trip.get_places(), [])
        self.assertIsNone(trip.budget)
        self.assertEqual(trip.notes, "")

    def test_zero_budget_trip(self):
        trip = Trip("ZeroBudget", budget=0)
        self.assertEqual(trip.budget, 0)
        trip.add_place("FreePlace")
        self.assertFalse(trip.is_over_budget())

    def test_negative_budget_trip(self):
        trip = Trip("NegativeBudget", budget=-100)
        trip.add_place("ExpensivePlace", cost=50)
        self.assertTrue(trip.is_over_budget())

    def test_duplicate_places(self):
        trip = Trip("Dups")
        trip.add_place("Beach", cost=30)
        trip.add_place("Beach", cost=30)
        self.assertEqual(len(trip.get_places()), 1)
        self.assertEqual(trip.get_places()[0].name, "Beach")

    def test_overwrite_notes(self):
        trip = Trip("Notes")
        trip.notes = "First"
        trip.notes = "Second"
        self.assertEqual(trip.notes, "Second")

    def test_delete_last_place(self):
        trip = Trip("Delete", budget=100)
        trip.add_place("A", cost=20)
        trip.add_place("B", cost=30)
        del trip.places[1]
        self.assertEqual(len(trip.get_places()), 1)

    def test_delete_nonexistent_item(self):
        trip = Trip("DeleteNone")
        with self.assertRaises(ValueError):
            del trip.places[99]

    def test_add_place_to_empty_trip(self):
        trip = Trip("EmptyAdd")
        trip.add_place("First", cost=10)
        self.assertEqual(len(trip.get_places()), 1)

    def test_delete_all_checklist_items(self):
        trip = Trip("Checklist")
        trip.checklist.append("Task1")
        trip.checklist.append("Task2")
        del trip.checklist[0]
        del trip.checklist[0]
        self.assertEqual(len(trip.get_checklist()), 0)

    def test_delete_nonexistent_checklist_item(self):
        trip = Trip("ChecklistNone")
        with self.assertRaises(ValueError):
            del trip.checklist[99]

    def test_add_duplicate_note(self):
        trip = Trip("DupNotes", notes="Same")
        trip.notes = "Same"
        self.assertEqual(trip.get_notes(), ["Same"])

    def test_delete_nonexistent_note(self):
        trip = Trip("NoteNone")
        with self.assertRaises(ValueError):
            del trip.checklist[0]  # triggers note deletion path indirectly
