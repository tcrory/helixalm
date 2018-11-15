"""helixalm constants."""


__version__ = '0.0.1'


# Helix ALM REST API: http://help.seapine.com/helixalm/rest-api/index.html
API_PATH = {

    # Projects                              Requests for retrieving and switching projects.
    'projects':                             '/projects',

    # Security                              Requests related to security.
    'security':                             '/{projectID}/token',

    # Rate Limits                           Requests related to rate limits.
    'rate_limits':                          '/{projectID}/ratelimits',

    # Issues                                Requests for viewing and updating issues.
    'issues':                               '/{projectID}/issues',
    'issues_search':                        '/{projectID}/issues/search',
    'issues_specific':                      '/{projectID}/issues/{itemID}',

    # Issue Attachments                     Requests for viewing and updating files attached to issues.
    'issues_attachments':                   '/{projectID}/issues/{itemID}/attachments',
    'issues_attachments_file':              '/{projectID}/issues/{itemID}/attachments/{attachmentID}',

    # Issue Events                          Requests for viewing and updating issue workflow events.
    'issues_events':                        '/{projectID}/issues/{itemID}/events',
    'issues_events_specific':               '/{projectID}/issues/{itemID}/events/{eventID}',
    'issues_events_attachments':            '/{projectID}/issues/{itemID}/events/{eventID}/attachments',
    'issues_events_attachments_file':       '/{projectID}/issues/{itemID}/events/{eventID}/attachments/{attachmentID}',

    # Issue foundByRecords                  Requests for viewing and updating issue Found by records.
    'issues_foundByRecords':                '/{projectID}/issues/{itemID}/foundByRecords',
    'issues_foundByRecords_specific':       '/{projectID}/issues/{itemID}/foundByRecords/{foundByRecordID}',
    'issues_foundByRecords_attachments':    '/{projectID}/issues/{itemID}/foundByRecords/{foundByRecordID}/attachments',
    'issues_foundByRecords_attachments_file': '/{projectID}/issues/{itemID}/foundByRecords/{foundByRecordID}/attachments/{attachmentID}',

    # Test Cases                            Requests for viewing and updating test cases.
    'test_cases':                           '/{projectID}/testcases',
    'test_cases_search':                    '/{projectID}/testcases/search',
    'test_cases_specific':                  '/{projectID}/testcases/{itemID}',

    # Test Case Attachments                 Requests for viewing and updating files attached to test cases.
    'test_cases_attachments':               '/{projectID}/testcases/{itemID}/attachments',
    'test_cases_attachments_file':          '/{projectID}/testcases/{itemID}/attachments/{attachmentID}',

    # Test Case Events                      Requests for viewing and updating test case workflow events.
    'test_cases_events':                    '/{projectID}/testcases/{itemID}/events',
    'test_cases_events_specific':           '/{projectID}/testcases/{itemID}/events/{eventID}',
    'test_cases_events_attachments':        '/{projectID}/testcases/{itemID}/events/{eventID}/attachments',
    'test_cases_events_attachments_file':   '/{projectID}/testcases/{itemID}/events/{eventID}/attachments/{attachmentID}',

    # Test Case Scripts                     Requests for viewing and updating scripts attached to test cases.
    'test_cases_scripts':                   '/{projectID}/testcases/{itemID}/scripts',

    # Test Case Steps                       Requests for viewing and updating test case steps.
    'test_cases_steps':                     '/{projectID}/testcases/{itemID}/steps',

    # Test Case Variants                    Requests for viewing and updating test case variants.
    'test_cases_variants':                  '/{projectID}/testcases/{itemID}/variants',

    # Test Runs                             Requests for viewing and updating test runs.
    'test_runs':                            '/{projectID}/testruns',
    'test_runs_generate':                   '/{projectID}/testruns/generate',
    'test_runs_search':                     '/{projectID}/testruns/search',
    'test_runs_specific':                   '/{projectID}/testruns/{itemID}',

    # Test Run Attachments                  Requests for viewing and updating files attached to test runs.
    'test_runs_attachments':                '/{projectID}/testruns/{itemID}/attachments',
    'test_runs_attachments_file':           '/{projectID}/testruns/{itemID}/attachments/{attachmentID}',

    # Test Run Events                       Requests for viewing and updating test run workflow events.
    'test_runs_events':                     '/{projectID}/testruns/{itemID}/events',
    'test_runs_events_specific':            '/{projectID}/testruns/{itemID}/events/{eventID}',
    'test_runs_events_attachments':         '/{projectID}/testruns/{itemID}/events/{eventID}/attachments',
    'test_runs_events_attachments_file':    '/{projectID}/testruns/{itemID}/events/{eventID}/attachments/{attachmentID}',

    # Test Run Scripts                      Requests for viewing and updating scripts attached to test runs.
    'test_runs_scripts':                    '/{projectID}/testruns/{itemID}/scripts',

    # Test Run Steps                        Requests for viewing and updating test run steps.
    'test_runs_steps':                      '/{projectID}/testruns/{itemID}/steps',

    # Test Run Variants                     Requests for viewing and updating test run variants.
    'test_runs_variants':                   '/{projectID}/testruns/{itemID}/variants',

    # Requirements                          Requests for viewing and updating requirements.
    'requirements':                         '/{projectID}/requirements',
    'requirements_search':                  '/{projectID}/requirements/search',
    'requirements_specific':                '/{projectID}/requirements/{itemID}',

    # Requirement Attachments               Requests for viewing and updating files attached to requirements.
    'requirements_attachments':             '/{projectID}/requirements/{itemID}/attachments',
    'requirements_attachments_file':        '/{projectID}/requirements/{itemID}/attachments/{attachmentID}',

    # Requirement Events                    Requests for viewing and updating requirement workflow events.
    'requirements_events':                  '/{projectID}/requirements/{itemID}/events',
    'requirements_events_specific':         '/{projectID}/requirements/{itemID}/events/{eventID}',
    'requirements_events_attachments':      '/{projectID}/requirements/{itemID}/events/{eventID}/attachments',
    'requirements_events_attachments_file': '/{projectID}/requirements/{itemID}/events/{eventID}/attachments/{attachmentID}',

    # Requirement Documents                 Requests for viewing requirement documents that contain a specific requirement.
    'requirements_documents':               '/{projectID}/requirements/{itemID}/documents',

    # Requirement Versions                  Requests for viewing requirement versions.
    'requirements_versions':                '/{projectID}/requirements/{itemID}/versions',

    # Documents                             Requests for viewing and udpating requirement documents.
    'documents':                            '/{projectID}/documents',
    'documents_search':                     '/{projectID}/documents/search',
    'documents_specific':                   '/{projectID}/documents/{itemID}',

    # Document Attachments                  Requests for viewing and updating files attached to requirement documents.
    'documents_attachments':                '/{projectID}/documents/{itemID}/attachments',
    'documents_attachments_file':           '/{projectID}/documents/{itemID}/attachments/{attachmentID}',

    # Document Events                       Requests for viewing and updating requirement document workflow events.
    'documents_events':                     '/{projectID}/documents/{itemID}/events',
    'documents_events_specific':            '/{projectID}/documents/{itemID}/events/{eventID}',
    'documents_events_attachments':         '/{projectID}/documents/{itemID}/events/{eventID}/attachments',
    'documents_events_attachments_file':    '/{projectID}/documents/{itemID}/events/{eventID}/attachments/{attachmentID}',

    # Document Snapshots                    Requests for creating and viewing requirement document snapshots.
    'documents_snapshots':                  '/{projectID}/documents/{itemID}/snapshots',

    # Document Trees                        Requests for viewing and updating requirement document trees.
    'document_trees':                       '/{projectID}/documentTrees/{itemID}',
    'document_trees_nodes':                 '/{projectID}/documentTrees/{itemID}/nodes',
    'document_trees_nodes_specific':        '/{projectID}/documentTrees/{itemID}/nodes/{nodeID}',
    'document_trees_nodes_child_nodes':     '/{projectID}/documentTrees/{itemID}/nodes/{nodeID}/childNodes',

    # Files                                 Requests for retrieving files.
    'files':                                '/{projectID}/files/{encodedFileID}',

    # Misc                                  Miscellaneous requests.
    'not_yet_implemented':                  '/NotYetImplemented'

}
