package Blackjack;

public class GenericPlayer {

	private String name;
	private ArrayList<Card> hand;
	private ArrayList<Card> hand2;

	public String getName() {
		return this.name;
	}

	/**
	 * 
	 * @param deck
	 */
	public void hit(Deck deck) {
		// TODO - implement GenericPlayer.hit
		throw new UnsupportedOperationException();
	}

	public void stand() {
		// TODO - implement GenericPlayer.stand
		throw new UnsupportedOperationException();
	}

	public ArrayList<Card> getHand() {
		return this.hand;
	}

	/**
	 * 
	 * @param newHand
	 */
	public void setHand(ArrayList<Card> newHand) {
		// TODO - implement GenericPlayer.setHand
		throw new UnsupportedOperationException();
	}

	public ArrayList<Card> getHand2() {
		// TODO - implement GenericPlayer.getHand2
		throw new UnsupportedOperationException();
	}

	/**
	 * 
	 * @param newHand
	 */
	public void setHand2(ArrayList<Card> newHand) {
		this.hand2 = newHand;
	}

	/**
	 * 
	 * @param deck
	 */
	public void hit(Deck deck) {
		// TODO - implement GenericPlayer.hit
		throw new UnsupportedOperationException();
	}

	public ArrayList<Card> getHand() {
		return this.hand;
	}

	public ArrayList<Card> getHand2() {
		// TODO - implement GenericPlayer.getHand2
		throw new UnsupportedOperationException();
	}

}