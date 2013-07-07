def _give_position_in_parent_from_donor_components_to_recipient_components(
    donors, recipients):
    '''When 'donors' has a parent, find parent.
    Then insert all components in 'recipients'
    in parent immediately before 'donors'.
    Then remove 'donors' from parent.

    When 'donors' has no parent, do nothing.

    Return 'donors'.

    Helper implements no spanner-handling at all.
    Helper is not composer-safe and may cause discontiguous spanners.
    '''
    from abjad.tools import componenttools
    from abjad.tools import selectiontools

    # check input
    assert componenttools.all_are_contiguous_components_in_same_parent(donors)
    assert componenttools.all_are_components(recipients)
    if not isinstance(donors, selectiontools.Selection):
        donors = selectiontools.Selection(donors)
    if not isinstance(recipients, selectiontools.Selection):
        recipients = selectiontools.Selection(recipients)

    parent, start, stop = \
        componenttools.get_parent_and_start_stop_indices_of_components(donors)

    if parent is None:
        return donors

    # to avoid pychecker slice assignment error
    #parent._music[start:start] = recipients
    parent._music.__setitem__(slice(start, start), recipients)
    recipients._set_component_parents(parent)
    donors._set_component_parents(None)

    return donors
