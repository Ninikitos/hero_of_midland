class TurnPace:
    """Singleton class to manage combat turn pacing."""

    def __new__(cls):
        """Create or return the existing instance of the TurnPace class."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(TurnPace, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        """Initialize the turn order and current turn state."""
        self.current_turn = None
        self.turn_order = []

    def set_turn_order(self, participants: list):
        """
        Define the combat turn order.

        Args:
            participants (list): List of combat characters.
        """
        self.turn_order = participants
        if participants:
            self.current_turn = participants[0]