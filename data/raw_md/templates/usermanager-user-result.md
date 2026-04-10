The `CreateUser` method returns a `UserResult` object. This object exposes the following properties:

`Succeeded`
:   A `boolean` property that indicates whether or not a user was created successfully.
`User`
:   The created user object.
`Error`
:   If user creation fails, this property contains the resulting @System.Exception.  