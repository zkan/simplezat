context('Rating', () => {
  beforeEach(() => {
    cy.visit('http://localhost:8000/ratings/')
  })

  it('should be able to give positve rating with comment', () => {
    cy.contains('How do we do?')
    cy.get('[href="positive/"] > img').should('have.attr', 'alt', 'Positive')
    cy.get('[href="neutral/"] > img').should('have.attr', 'alt', 'Neutral')
    cy.get('[href="negative/"] > img').should('have.attr', 'alt', 'Negative')

    cy.get('img[alt="Positive"]').click()
    cy.wait(1000)

    cy.contains('Any comment?')
    cy.get('textarea[name="comment"]').type('You are doing great!')
    cy.get('button').click()
    cy.wait(1000)

    cy.contains('Thank you!')
  })
})
