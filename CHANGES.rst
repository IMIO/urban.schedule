Changelog
=========

.. You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst

.. towncrier release notes start

1.0.0a3 (2024-03-30)
--------------------

New features:


- Store checking completion task config for liege.
  Store reception task config for CODT Buildlicence and CU on Urban classic.
  [daggelpop, mpeeters] (URB-3005)


Internal:


- Add french translations for conditions.
  Handle specific configuration for Liege and Urban classic.
  Improve import of config by adding `match_filename` optional parameter to only import one config filename.
  [mpeeters] (URB-3005)


1.0.0a2 (2024-03-14)
--------------------

Bug fixes:


- Fix import uid and @id and fix existing content handling
  Fix enum dependency
  [jchandelle] (URB-3005)


1.0.0a1 (2024-03-12)
--------------------

New features:


- Add conditions to determine if the current content is under the new reform or not
  [mpeeters] (URB-3004)
- Add upgrade step to import schedule config
  Adapt `urban.schedule.start_date.acknowledgment_limit_date` to handle the new rules of the CODT reform
  [jchandelle, mpeeters] (URB-3005)
