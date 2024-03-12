Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

1.0.0a1 (2024-03-12)
--------------------

New features:


- Add conditions to determine if the current content is under the new reform or not
  [mpeeters] (URB-3004)
- Add upgrade step to import schedule config
  Adapt `urban.schedule.start_date.acknowledgment_limit_date` to handle the new rules of the CODT reform
  [jchandelle, mpeeters] (URB-3005)
