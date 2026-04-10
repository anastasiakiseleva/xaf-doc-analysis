> [!Important]
> In EF Core-based projects, the XAF Security System requires that [Change Tracking](https://learn.microsoft.com/en-us/ef/core/change-tracking/) is active when you work with DbContext.
>
> If LINQ Expressions call the `AsNoTracking()` or `AsNoTrackingWithIdentityResolution()` method, or if Change Tracking is otherwise deactivated, a data request becomes unsafe (may result in unauthorized data access).
