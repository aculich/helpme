'''


Copyright (C) 2017-2018 Vanessa Sochat.
Copyright (C) 2017-2018 The Board of Trustees of the Leland Stanford Junior
University.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

def get_helper(quiet=False, **kwargs):
    '''
       get the correct helper depending on the environment variable
       HELPME_CLIENT

       quiet: if True, suppress most output about the client (e.g. speak)

    '''
    from helpme.defaults import HELPME_CLIENT

    # If no obvious credential provided, we can use HELPME_CLIENT
    if   HELPME_CLIENT == 'github': from .github import Helper
    elif HELPME_CLIENT == 'uservoice': from .uservoice import Helper
    else: from .github import Helper

    Helper.name = HELPME_CLIENT
    Helper.quiet = quiet

    # Create credentials cache, if it doesn't exist
    Helper._credential_cache = get_credential_cache()

    from helpme.action import ( record, config )
    Helper.add = add
    Helper._init_db = init_db        

    # Initialize the database
    return Helper()

Helper = get_client()
