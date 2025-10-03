"""
    This package is used only with exercises and examples that make network requests
    using requests.get().  This happens, for example, in ch06_api\02_using_requests.

    To use it, uncomment the import mocklab statement in the source file.

    mocklab should not be needed if internet access is available.

    Finally, in order to use mocklab, the student_files directory MUST be present on your
    PYTHONPATH.
"""
import sys

from .patcher import patch, RequestsGet


try:
    import requests
except ImportError:
    print('The requests module must first be installed before using mocklab.', file=sys.stderr)
    sys.exit(42)


patch(requests, 'get', RequestsGet())
