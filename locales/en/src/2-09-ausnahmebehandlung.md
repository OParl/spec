## Exception Handling
{#ausnahmebehandlung}

If a server can not handle a request, e.g. because the
URL is invalid or the requested object does not exist, it ** should **
respond with the appropriate HTTP status code.

In this case, a server ** should ** return an object containing the following
3 attributes:

 * `type`: Contains the URL `https://schema.oparl.org/1.1/Error` as value
 * `message`: An error message to display for a user
 . Therefore, the error message should be in the language of the
 content that is delivered through the interface.
 * `debug`: Additional information about the bug

 If a server outputs such an object, then ** it ** must
 send an HTTP status code indicating an error.

 A client ** may not ** assume that in a case of a mistake, the status code
 contains useful information such as the error object described above.
