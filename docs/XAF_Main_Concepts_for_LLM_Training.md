# XAF Main Concepts for LLM Training

This document identifies the main concepts, components, and terminology used in DevExpress eXpressApp Framework (XAF) documentation. These concepts are essential for training a language model to perform semantic analysis of XAF documentation.

---

## 1. Core Architecture & Framework Fundamentals

### 1.1 Plug-in MVC Architecture
- **Application Framework**: Cross-platform .NET App UI & Web API framework
- **Model-View-Controller (MVC) Pattern**: Separation of business logic from visual representation
- **Platform Independence**: Same business logic runs on WinForms, Blazor, and legacy ASP.NET Web Forms
- **Plug-in Architecture**: Modular, extensible design using modules

### 1.2 Application Solution Components
- **Application Solution Structure**: Multi-project solution organization
- **Modules**: Reusable functional blocks (System Module, Platform-specific modules, Extra modules)
- **Module Registration**: Ways to register built-in and custom XAF modules
- **Shared Modules**: Reuse modules between .NET Framework and .NET applications

### 1.3 Platform Support
- **UI Platforms**:
  - **Blazor UI** (ASP.NET Core Blazor) - Modern web UI for .NET
  - **WinForms** (.NET and .NET Framework) - Desktop UI
  - **ASP.NET Web Forms** (.NET Framework) - Legacy web UI
- **Backend Web API Service**: REST API, OData endpoints, CRUD operations
- **Middle Tier Architecture**: Client-server with security enforcement

---

## 2. Data Layer & ORM (Object-Relational Mapping)

### 2.1 ORM Frameworks
- **Entity Framework Core (EF Core)**: Recommended for new development
- **XPO (eXpress Persistent Objects)**: DevExpress proprietary ORM
- **ORM Layer**: Abstraction over database operations
- **Database Providers**: SQL Server, PostgreSQL, MySQL, SQLite, Oracle, etc.

### 2.2 Business Model Design
- **Business Classes**: Classes that define data entities (POCOs or persistent classes)
- **Persistent Objects**: Classes mapped to database tables
- **Non-Persistent Objects**: In-memory objects not stored in database
- **Business Class Library**: Built-in base classes (Person, Organization, Event, etc.)
- **Data Annotations**: Attributes for metadata and validation

### 2.3 Property Types
- **Key Properties**: Primary keys and identifiers
- **String Properties**: Text data with size attributes
- **Numeric Properties**: Integer, decimal, floating-point
- **Date and Time Properties**: DateTime, DateTimeOffset
- **Boolean Properties**: True/false values
- **BLOB Image Properties**: Binary image data
- **File Attachment Properties**: Document and file storage
- **Collection Properties**: One-to-many relationships
- **Reference Properties**: Foreign key, many-to-one relationships (Lookup editors)
- **Complex Type Properties**: Nested value objects
- **Enumeration Properties**: Predefined value lists
- **Type Properties**: System.Type metadata
- **Criteria Properties**: Filter expressions
- **Color Properties**: UI color values
- **Calculated Properties**: Computed values based on other properties

### 2.4 Relationships
- **One-to-Many Relationships**: Single parent, multiple children
- **Many-to-Many Relationships**: Multiple associations on both sides
- **Aggregated Relationships**: Composition, lifecycle dependency
- **Reference (Foreign Key) Relationships**: Navigation properties
- **Dependent Reference Properties**: Cascading lookups

### 2.5 Data Operations
- **Object Space**: Unit of Work pattern for data operations
- **ObjectSpace Provider**: Factory for creating ObjectSpace instances
- **CRUD Operations**: Create, Read, Update, Delete
- **Optimistic Locking**: Concurrency control (EF Core, XPO)
- **Data Locking**: Pessimistic and optimistic concurrency control
- **Change Tracking**: Detect and track object modifications
- **Property Change Notifications**: INotifyPropertyChanged pattern
- **Refresh and Rollback**: Undo changes and reload from database

### 2.6 Database Schema
- **Code First**: Generate database from business classes
- **Database First**: Generate business classes from existing database
- **Migrations**: Database schema versioning and updates (EF Core)
- **Database Updates**: Automatic schema synchronization
- **Connection String**: Database connection configuration

---

## 3. Application Model (Metadata & UI Settings)

### 3.1 Application Model Fundamentals
- **Application Model**: Metadata repository defining navigation, data presentation, and commands
- **Model Nodes**: Hierarchical structure of UI and behavior settings
- **Model Editor**: Design-time and runtime visual editor for Application Model
- **XAFML Files**: XML-based Application Model storage format
- **Model Differences**: Customizations stored separately from defaults

### 3.2 Model Node Types
- **ViewItems**: Elements within Views
- **Views**: List Views, Detail Views, Dashboard Views
- **Controllers**: Logic and behavior containers
- **Actions**: Menu commands and toolbar buttons
- **Navigation Items**: Navigation structure definition
- **BOModel (Business Object Model)**: Business class metadata
- **Filters**: Predefined filter criteria
- **Options**: Application-wide settings

### 3.3 Model Interfaces
- **IModelApplication**: Root application model interface
- **IModelViews**: Collection of all Views
- **IModelClass**: Business class metadata
- **IModelMember**: Property metadata
- **Built-in Model Interfaces**: Typed access to Application Model nodes

### 3.4 Model Generators
- **Node Generators**: Automatic population of Application Model from code
- **Generator Updaters**: Extend or modify generated nodes
- **Built-in Node Generators**: Class, Member, ListView, DetailView generators

### 3.5 Model Customization
- **Design-Time Customization**: Model Editor in Visual Studio
- **Runtime Customization**: End-user model differences
- **Code Customization**: Access and modify Application Model in code
- **Model Storage**: Database-stored user preferences
- **Model Merge Tool**: Combine model differences

---

## 4. User Interface Construction

### 4.1 Views
- **List View**: Displays collections of objects (grids, lists)
- **Detail View**: Displays single object with property editors
- **Dashboard View**: Multiple views side-by-side on one screen
- **Nested List View**: Collection property displayed within Detail View
- **Lookup List View**: Selection dialog for reference properties

### 4.2 List View Features
- **List View Data Access Modes**:
  - Client Mode: Load all data to client
  - Server Mode: Server-side data processing
  - ServerView Mode: Server with client-side grouping
  - Queryable Mode: LINQ query composition
  - DataView Mode: DataView for disconnected scenarios
  - InstantFeedback Mode: Virtual mode for large datasets
- **List View Edit Modes**: View mode, Edit mode, In-place editing
- **Column Generation**: Automatic column creation from properties
- **Column Customization**: Reorder, hide, format columns
- **Banded Layout**: Group columns into bands
- **Row Preview**: Show additional details below rows
- **Asynchronous Loading**: Background data loading (WinForms)

### 4.3 Detail View Features
- **Layout Generation**: Automatic layout from properties
- **Layout Customization**: Tabs, groups, columns arrangements
- **Layout Control**: WinForms LayoutControl, Blazor layout components
- **Runtime Layout Customization**: End-user layout changes
- **Nested Property Editors**: Display related object properties inline

### 4.4 Property Editors
- **Property Editor**: UI control bound to a business class property
- **Built-in Property Editors**: Standard editors for each data type
- **Custom Property Editors**: User-defined editors
- **Lookup Editor**: Dropdown/search for reference properties
- **Cascading Lookups**: Dependent lookup filtering
- **Complex Property Editor**: Editor for complex type properties
- **Blob Property Editor**: Display images and binary data

### 4.5 View Items
- **Action Container View Item**: Host Actions in View layout
- **Control View Item**: Embed custom controls in View
- **Custom View Item**: User-defined View elements
- **Static Text/Image**: Display non-editable content

---

## 5. Controllers & Actions (Business Logic & UI Commands)

### 5.1 Controllers
- **Controller**: Container for logic, Actions, and UI customization
- **View Controller**: Operates on specific View types (ListView, DetailView)
- **Window Controller**: Operates on Windows/Frames
- **Object Controller**: Operates on specific object types
- **Generic Controller**: Works with any View or object
- **Controller Activation**: Context-based enabling/disabling
- **Controller Scope**: Define where Controllers are active

### 5.2 Actions (Menu Commands)
- **Action**: User interaction abstraction (buttons, menu items)
- **Simple Action**: Execute single command
- **Parametrized Action**: Command with parameters (editor input)
- **Single Choice Action**: Select one option from list
- **Popup Window Show Action**: Open dialog with View
- **Action Context**: Current View, selected objects, ObjectSpace
- **Action Activation**: Context-based enabling/disabling

### 5.3 Built-in Actions
- **New**: Create new object
- **Save**: Commit changes to database
- **Delete**: Remove objects
- **Refresh**: Reload data
- **Export**: Export data to Excel, CSV, etc.
- **Print**: Print list or detail
- **Full-Text Search**: Search across properties
- **Link/Unlink**: Manage many-to-many relationships
- **Navigation Actions**: Navigate to different Views

### 5.4 Action Customization
- **Action Attribute**: Declare Actions declaratively
- **Action Containers**: Toolbar, menu, navigation areas
- **Action Location**: Control where Actions appear
- **Action Order**: Arrange Actions in containers
- **Custom Actions**: User-defined Actions

---

## 6. Navigation System

### 6.1 Navigation Structure
- **Navigation Items**: Root items, folders, nested items
- **Navigation Control**: Tree or tiles UI for navigation
- **Office Navigation Bar**: Bottom bar with buttons
- **Default Object View**: Auto-navigate to Detail View
- **Start-up Navigation Item**: Initial View on app launch
- **Context Navigation**: Navigate from current object

### 6.2 Navigation Customization
- **Add Navigation Items**: Define in Application Model or code
- **Rename Navigation Items**: Customize labels
- **Rearrange Navigation**: Reorder items and folders
- **Show/Hide Navigation Items**: Conditional visibility
- **Custom Navigation**: Implement custom navigation logic

---

## 7. Windows, Frames & Templates

### 7.1 Windows and Frames
- **Window**: Top-level container (main window, popup)
- **Frame**: Container for Views within a Window
- **Main Window**: Primary application window
- **Popup Window**: Dialog for Detail Views or custom content
- **Nested Frame**: Embedded Frame within a View

### 7.2 Templates
- **Application Template**: Main window layout structure
- **Blazor Templates**: Razor components for Blazor UI
- **WinForms Templates**: UserControl-based templates for WinForms
- **Ribbon Template**: Office-style ribbon interface
- **Standard Template**: Classic toolbar/menu
- **Custom Templates**: User-defined application shells
- **Tabbed MDI**: Multiple document interface with tabs
- **SDI (Single Document Interface)**: One View at a time

### 7.3 Template Features
- **Action Containers**: Locations for Actions (toolbar, menu)
- **Navigation Panel**: Area for Navigation Control
- **View Site**: Area where Views are displayed
- **Status Bar**: Bottom status messages
- **Template Customization**: Modify appearance and layout

---

## 8. Data Filtering & Querying

### 8.1 Filtering Mechanisms
- **Criteria Property**: Filter expression on CollectionSource
- **Application Model Criteria**: Define filters in metadata
- **Filters Node**: Predefined filters for List Views
- **ListViewFilter Attribute**: Code-based filter definitions
- **Full-Text Search**: Search across multiple properties
- **Auto Filter Row**: Excel-like column filtering (grids)

### 8.2 Criteria Language
- **Criteria Operators**: Building blocks for filter expressions
- **Function Operators**: Built-in functions (Contains, StartsWith, etc.)
- **Custom Function Operators**: User-defined functions
- **Object Parameters**: Use objects as filter values
- **Current Object Parameter**: Filter based on current object
- **Parse String Criteria**: Text-based filter expressions

### 8.3 Data Sources
- **Collection Source**: Data source for List Views
- **Data Source Criteria**: Filter applied to data source
- **Lookup List View Data Source**: Filter options in lookups
- **Cascading Filtering**: Hierarchical filter dependencies
- **Server-Side Filtering**: Filtering at database level

---

## 9. Security System

### 9.1 Security Architecture
- **Authentication**: User identity verification
- **Authorization**: Access control based on permissions
- **Security System**: Comprehensive role-based access control
- **Security Strategy**: Defines permission model

### 9.2 Security Tiers
- **2-Tier Security (Integrated Mode)**: Direct database access with security
- **UI Level Security**: Client-side security checks (legacy, less secure)
- **Middle Tier Security**: Server enforces permissions (EF Core, XPO)
- **Backend Web API Security**: JWT, OAuth2 authentication

### 9.3 User and Role Management
- **User Objects**: ApplicationUser, PermissionPolicyUser
- **Role Objects**: PermissionPolicyRole
- **Administrator Role**: Full access role
- **Custom User/Role Objects**: Extend default security objects
- **Active Directory Integration**: Windows authentication
- **OAuth2 Providers**: Azure AD, Google, Facebook authentication
- **JWT Authentication**: Token-based authentication for Web API

### 9.4 Permission Types
- **Type Permissions**: Access to entire class (Read, Write, Create, Delete, Navigate)
- **Object Permissions**: Access to specific object instances
- **Member Permissions**: Field-level permissions (Read, Write)
- **Operation Permissions**: Custom permission checks
- **Criteria-Based Permissions**: Filter objects by criteria

### 9.5 Security Features
- **Role-Based Security**: Users assigned to roles with permissions
- **Permission Policy**: Allow or deny specific operations
- **Permission Merging**: Combine permissions from multiple roles
- **Associated Object Permissions**: Permissions for related objects
- **Security System Check**: Verify permissions in code
- **Current User**: Access authenticated user in code
- **Password Policies**: Password complexity validation
- **Logon Window**: Standard authentication UI
- **Security Caching**: Performance optimization

---

## 10. Validation Module

### 10.1 Validation Concepts
- **Validation Rules**: Constraints on business object properties
- **Validation Contexts**: When validation is triggered (Save, Delete, Custom)
- **Validation Attributes**: Declare rules on properties
- **Rule Properties**: Configuration for validation rules

### 10.2 Built-in Validation Rules
- **RuleRequiredField**: Required property
- **RuleRegularExpression**: Pattern matching
- **RuleRange**: Numeric or date range
- **RuleStringComparison**: String length constraints
- **RuleCriteria**: Complex criteria-based validation
- **RuleFromBoolProperty**: Validation from boolean property
- **RuleUniqueValue**: Ensure uniqueness
- **RuleValueComparison**: Compare two property values
- **RuleObjectExists**: Check related object existence
- **RuleIsReferenced**: Verify object has no references

### 10.3 Validation Features
- **Collection Validation**: Validate collection items
- **Custom Validation Rules**: User-defined validators
- **Localized Messages**: Translate validation messages
- **Programmatic Validation**: Trigger validation in code
- **Validation State**: Track validation errors
- **Warning vs Error**: Severity levels

---

## 11. Conditional Appearance Module

### 11.1 Conditional Appearance Concepts
- **Appearance Attribute**: Declare appearance rules on classes
- **Appearance Rules**: Conditional UI element state changes
- **Criteria**: Boolean expression to determine when rule applies
- **Target Items**: Properties, Actions, or Views affected

### 11.2 Appearance Actions
- **Enable/Disable**: Control element interactivity
- **Show/Hide**: Control element visibility
- **Highlight**: Change background or font color
- **Font Style**: Bold, italic, strikethrough
- **Custom Appearance**: User-defined styling

### 11.3 Contexts
- **List View Context**: Appearance in grid rows
- **Detail View Context**: Appearance in property editors
- **View Level**: Apply to entire View
- **Property Level**: Apply to specific property editors

---

## 12. Reports Module

### 12.1 Reporting Concepts
- **Reports V2 Module**: Modern reporting engine
- **XtraReports**: DevExpress reporting component
- **Report Designer**: Visual report design tool
- **Report Data Sources**: Business objects, collections, non-persistent
- **Report Parameters**: User input for filtering
- **Predefined Reports**: Static reports defined at design time
- **User Reports**: Runtime-created reports stored in database

### 12.2 Report Features
- **Report Preview**: View before printing
- **Export Formats**: PDF, Excel, Word, HTML, RTF, etc.
- **Report Actions**: ShowReportsListView, ShowReportDesigner, PrintReport
- **In-Place Reports**: Reports embedded in Views
- **Report Designer Control**: WinForms and Blazor designers
- **Grid-Based Reporting**: Export grids to reports (WinForms)

### 12.3 Report Customization
- **Custom Report Storage**: Customize report persistence
- **Report Scripts**: C# or VB.NET code in reports
- **Calculated Fields**: Formula-based fields
- **Master-Detail Reports**: Hierarchical data
- **Subreports**: Embed reports within reports
- **Report Parameters Validation**: Validate user input

---

## 13. Pivot Grid and Analysis Module

### 13.1 Pivot Grid Concepts
- **Pivot Grid Module**: OLAP-style data analysis
- **Pivot Field**: Column, row, or data aggregation
- **Pivot Editor**: Configure pivot grid at runtime
- **Drill Down**: Navigate to underlying data

### 13.2 Chart Module
- **Chart View**: Visualize data as charts
- **Chart Types**: Bar, line, pie, area, etc.
- **Chart Editor**: Configure charts at runtime
- **Chart Data Binding**: Bind to business objects

### 13.3 Pivot Chart (Analysis) Module
- **Combined Pivot and Chart**: Interactive analysis
- **Analysis Dashboard**: Multiple analytical views

---

## 14. Dashboards Module

### 14.1 Dashboard Concepts
- **Dashboard**: Multiple views and visualizations on one screen
- **Dashboard Designer**: Visual dashboard design tool
- **Dashboard Items**: Charts, grids, gauges, maps, etc.
- **Dashboard Data Sources**: Business objects, SQL queries
- **Dashboard Parameters**: User input for filtering

### 14.2 Dashboard Features
- **Predefined Dashboards**: Static dashboards defined at design time
- **User Dashboards**: Runtime-created dashboards
- **Dashboard Actions**: ShowDashboard, EditDashboard
- **Interactivity**: Master-filter, drill-down
- **Export**: PDF, Image formats
- **Dashboard Extensions**: Custom dashboard items

### 14.3 Platform-Specific
- **Blazor Dashboard**: HTML5 dashboard in Blazor UI
- **WinForms Dashboard**: Native dashboard in Windows
- **Dashboard REST services**: Web-based dashboard backend

---

## 15. Scheduler Module

### 15.1 Scheduler Concepts
- **Scheduler Module**: Calendar and appointment management
- **Event Class**: Business class for appointments (Event, built-in)
- **Resources**: Assign events to resources (rooms, people)
- **Recurring Events**: Repeating appointments
- **Exceptional Occurrences**: Modified instances of recurring events

### 15.2 Scheduler Features
- **Scheduler Views**: Day, Week, Month, Timeline, Agenda
- **Scheduler Actions**: New appointment, edit, delete
- **Appointment labeling**: Status, label properties
- **Reminders**: Notifications for upcoming events
- **Time zones**: Multi-timezone support
- **Scheduler Control**: DevExpress SchedulerControl

---

## 16. Notifications Module

### 16.1 Notification Concepts
- **Notifications Module**: Reminders and alerts
- **ISupportNotifications**: Interface for notification-enabled classes
- **Reminders Window**: Display upcoming reminders
- **Notifications Service**: Background processing
- **Notification Providers**: Pluggable notification delivery

### 16.2 Notification Features
- **Postpone/Dismiss**: Snooze or dismiss reminders
- **Custom Notifications**: User-defined notification logic
- **Multi-User Notifications**: Target specific users
- **Notification Localization**: Translate notification text

---

## 17. State Machine Module

### 17.1 State Machine Concepts
- **State Machine Module**: Manage object state transitions
- **States**: Defined states for objects (New, InProgress, Completed)
- **Transitions**: Allowed state changes
- **Transition Actions**: Code executed during transitions
- **IStateMachine Interface**: Implement state machine on classes

### 17.2 Transition Types
- **User-Defined Transitions**: Runtime-defined transitions
- **Predefined Transitions**: Design-time defined in code
- **Conditional Transitions**: Criteria-based availability

---

## 18. Workflow Module

### 18.1 Workflow Concepts
- **Workflow Module**: Windows Workflow Foundation (WF) integration
- **Workflow Activities**: Reusable workflow actions
- **Workflow Designer**: Visual workflow design
- **Workflow Service**: Background workflow execution

### 18.2 Workflow Features
- **Sequential Workflows**: Step-by-step execution
- **State Machine Workflows**: State-based workflows
- **Custom Activities**: User-defined workflow actions
- **Workflow Persistence**: Save workflow state

---

## 19. Audit Trail Module

### 19.1 Audit Concepts
- **Audit Trail Module**: Track data changes
- **Audit Log**: History of all modifications
- **Audited Objects**: Objects tracked for changes
- **Audit Properties**: Properties tracked within objects

### 19.2 Audit Features
- **Audit Operations**: Track Create, Read, Update, Delete
- **Old/New Values**: Compare before and after
- **User/Host Identity**: Who made changes
- **Custom Audit Data**: Additional audit information
- **Audit Analysis**: Review audit log
- **Change History**: View object's change timeline

### 19.3 Platform Support
- **EF Core Audit Trail**: Entity Framework Core implementation
- **XPO Audit Trail**: XPO implementation

---

## 20. Multi-Tenancy Module

### 20.1 Multi-Tenancy Concepts
- **Multi-Tenancy**: Multiple independent tenants in one application
- **Tenant**: Isolated data partition (customer, organization)
- **Tenant Resolver**: Identify current tenant
- **Tenant-Specific Data**: Data isolation per tenant
- **Shared Data**: Data accessible across tenants

### 20.2 Multi-Tenancy Features
- **Tenant Database**: Separate databases per tenant or shared database
- **Tenant Context**: Current tenant in code
- **Tenant Switching**: Change active tenant
- **Tenant-Aware Security**: Permissions per tenant

---

## 21. File Attachments Module

### 21.1 File Attachment Concepts
- **File Attachments Module**: Manage document uploads
- **FileData Class**: Built-in class for file storage
- **File Property Editor**: Upload/download UI
- **File Storage**: Database or file system

### 21.2 File Features
- **Multiple Attachments**: Collection of files per object
- **File Preview**: View documents inline
- **Download Action**: Download files in Blazor
- **Custom Upload UI**: Popup for file uploads

---

## 22. Clone Object Module

### 22.1 Clone Concepts
- **Clone Object Module**: Duplicate objects
- **Clone Action**: Built-in action to clone objects
- **ICloneable**: Interface for cloneable objects
- **Deep Clone**: Copy related objects

---

## 23. Office Module

### 23.1 Office Features
- **Rich Text Editor**: DevExpress RichEditControl
- **Spreadsheet Editor**: DevExpress SpreadsheetControl
- **PDF Viewer**: DevExpress PdfViewerControl
- **Document Properties**: Store documents in business objects
- **Mail Merge**: Merge data into documents

### 23.2 Office Customization
- **Access Rich Text Control**: Customize editor
- **Access Spreadsheet Control**: Customize editor
- **Document Templates**: Predefined document formats

---

## 24. TreeList Editor Module

### 24.1 TreeList Concepts
- **TreeList Module**: Hierarchical data display
- **ITreeNode Interface**: Self-referencing hierarchy
- **HCategory Class**: Built-in hierarchical class
- **Flat Data TreeList**: Display hierarchical data from flat structure
- **Categorized List**: Group objects hierarchically
- **Node Images**: Icons in tree nodes

---

## 25. View Variants Module

### 25.1 View Variants Concepts
- **View Variants**: Multiple layouts for same View
- **Variant**: Named configuration (columns, filters, sorting)
- **Switch Variants**: User selects variant at runtime
- **Variant Actions**: Change View Variant action

---

## 26. Layout Management

### 26.1 Layout Concepts
- **Detail View Layout**: Property arrangement in Detail Views
- **List View Layout**: Column arrangement in List Views
- **Layout Control**: WinForms LayoutControl for flexible layouts
- **Layout Groups**: Group properties into tabs, groups, columns
- **Layout Items**: Individual property editors in layout

### 26.2 Layout Customization
- **Design-Time Layout**: Model Editor customization
- **Runtime Layout**: End-user customization
- **Layout Persistence**: Save user layout changes

---

## 27. Localization & Accessibility

### 27.1 Localization
- **Localization**: Multi-language support
- **Resource Localization**: Translate UI strings
- **Localization Tool**: Extract and translate strings
- **Culture-Specific Formatting**: Date, number, currency formats
- **Runtime Language Switcher**: Change language at runtime
- **Custom Translation Provider**: Integrate translation services

### 27.2 Accessibility
- **Screen Reader Support**: Assistive technology compatibility
- **Keyboard Navigation**: Full keyboard support
- **High Contrast**: Support for high contrast themes
- **ARIA Attributes**: Accessibility markup (Blazor)

---

## 28. Deployment & Distribution

### 28.1 Deployment Scenarios
- **IIS Deployment**: ASP.NET Core Blazor on IIS
- **Azure Deployment**: Cloud deployment
- **Linux Deployment**: Nginx hosting
- **WinForms Xcopy**: Copy binaries
- **ClickOnce**: WinForms deployment
- **Setup Projects**: Installer-based deployment

### 28.2 Production Database
- **Database Updates**: Apply schema changes in production
- **Connection String Configuration**: Separate dev/prod settings
- **Database Security**: Secure connection strings
- **ModuleInfo Table**: Track application versions

---

## 29. Testing & Debugging

### 29.1 Testing
- **Unit Tests**: Test business logic
- **End-to-End Tests**: UI testing with EasyTest or xUnit
- **EasyTest**: Human-readable test scripts
- **xUnit + Selenium**: Web UI testing
- **Functional Tests**: Test complete scenarios
- **Screenshot Tests**: Visual regression testing

### 29.2 Debugging
- **Log Files**: Application event logging
- **Diagnostic Information**: Collect troubleshooting data
- **Tracer**: Custom log entries
- **Model Merge Tool**: Debug model differences
- **Debugger Integration**: Visual Studio debugging

### 29.3 Code Analysis
- **Roslyn Analyzers**: Automatic code error detection
- **XAF-Specific Analyzers**: XAF0001-XAF0034 error codes
- **Code Diagnostics**: Best practices enforcement

---

## 30. Performance Optimization

### 30.1 Database Performance
- **Indexing**: Database index optimization
- **Query Optimization**: Efficient LINQ queries
- **Eager Loading**: Load related data upfront (EF Core)
- **Lazy Loading**: On-demand data loading
- **Query Splitting**: Separate queries for collections (EF Core)

### 30.2 ORM Performance
- **Change Tracking**: Minimize tracking overhead
- **Batch Updates**: Group database operations
- **Connection Pooling**: Reuse connections
- **Deferred Loading**: Delay data retrieval
- **Server Mode**: Server-side data processing

### 30.3 Application Performance
- **Asynchronous Loading**: Load data in background (WinForms)
- **Virtual Mode**: Render only visible rows
- **InstantFeedback Mode**: Virtual scrolling for large datasets
- **Caching**: Security permissions, static data

---

## 31. Advanced Features

### 31.1 Dependency Injection (DI)
- **Service Registration**: Register services in DI container
- **Constructor Injection**: Inject services into Controllers
- **IObjectSpace Injection**: Access data layer in services
- **Application Builder**: Configure DI in .NET applications

### 31.2 Application Builder Pattern
- **Application Builder**: Modern .NET application initialization
- **Service Configuration**: Configure services fluently
- **Module Registration**: Fluent module API
- **Options Pattern**: Strongly-typed configuration

### 31.3 Types Info Subsystem
- **ITypesInfo**: Runtime type metadata
- **Type Discovery**: Find types at runtime
- **Dynamic Attributes**: Add attributes dynamically
- **Custom Persistent Fields**: Runtime-defined properties

### 31.4 Custom Object Space Provider
- **Custom Data Sources**: Non-database data sources
- **External APIs**: Integrate external systems
- **Adapter Pattern**: Wrap existing data access

---

## 32. UI Platform-Specific Features

### 32.1 Blazor-Specific
- **Blazor Components**: Underlying DevExpress Blazor controls
- **Blazor Templates**: Razor component templates
- **CSS Styles**: Custom styling with CSS
- **Themes**: Built-in and custom themes
- **Hot Reload**: Real-time development updates
- **Content Security Policy (CSP)**: Security headers
- **Error Handling**: Global error boundary
- **Loading Panels**: Display during operations
- **Popup Dialog Customization**: Size and style
- **Ribbon UI**: Office-style ribbon interface

### 32.2 WinForms-Specific
- **High DPI Support**: 4K display scaling
- **DPI-Aware**: Per-monitor DPI awareness
- **DevExpress Skins**: Visual themes
- **Document Manager**: MDI management
- **Bar Manager**: Toolbar and menu management
- **Ribbon Control**: Office-style ribbon
- **Layout Control**: Flexible form layouts
- **Splash Screen**: Startup screen

---

## 33. Web API & Backend Services

### 33.1 Backend Web API Service
- **REST API**: Create HTTP endpoints
- **OData**: Query protocol support
- **CRUD Endpoints**: Auto-generated API endpoints
- **Authentication**: JWT, OAuth2
- **Authorization**: Permission-based access
- **Custom Endpoints**: User-defined API methods
- **Swagger**: API documentation and testing
- **Deep Update**: Complex object graphs
- **Batch Operations**: Multiple operations in one request

### 33.2 Web API Features
- **Endpoint Customization**: Modify response/request
- **Business Object Methods**: Expose as endpoints
- **Non-Persistent Objects**: API for in-memory objects
- **Validation**: Validate Web API input
- **File Upload/Download**: BLOB operations via API
- **Localization Endpoint**: Retrieve translations via API

---

## 34. AI & Modern Features

### 34.1 AI Integration
- **AI-Powered Features**: Leverage AI capabilities in XAF applications
- **Smart Recommendations**: AI-driven suggestions
- **Natural Language Processing**: Parse user queries

---

## 35. Migration & Compatibility

### 35.1 .NET Migration
- **Port from .NET Framework**: Migrate legacy applications to .NET
- **Shared Module Compatibility**: Reuse modules across frameworks
- **Legacy API Removal**: Phase out .NET Framework APIs
- **Combined Solutions**: WinForms and Blazor in one solution

### 35.2 Version Management
- **Version History**: Release notes and changes
- **Upgrade Guide**: Update between versions
- **Breaking Changes**: API changes between versions
- **ModuleInfo**: Track application version in database

---

## 36. DevExpress Components Integration

### 36.1 UI Components
- **DXperience Subscription**: Full DevExpress component suite
- **Data Grid**: Advanced grid controls
- **Editors**: Rich property editors
- **Charts**: Visualization components
- **Reports**: XtraReports engine
- **Dashboards**: Dashboard Designer and Viewer
- **Scheduler**: Appointment scheduling

### 36.2 Component Customization
- **Access Underlying Controls**: Direct control access for customization
- **Component Settings**: Configure DevExpress components
- **Custom Components**: Integrate non-DevExpress controls

---

## 37. Business Logic Patterns

### 37.1 Common Patterns
- **Calculated Properties**: Derived values from other properties
- **Dependent Properties**: Properties that depend on other properties
- **Property Initialization**: Set default values
- **Business Rule Validation**: Enforce business constraints
- **Event Handlers**: Respond to object lifecycle events

### 37.2 Data Manipulation
- **ObjectSpace Pattern**: Unit of Work for transactional operations
- **Refresh/Reload**: Sync with database
- **Commit Changes**: Save to database
- **Rollback**: Undo unsaved changes
- **Nested ObjectSpace**: Isolated transactions

---

## 38. Extensibility & Customization

### 38.1 Extension Points
- **Custom Modules**: Package reusable functionality
- **Custom Controllers**: Add logic and Actions
- **Custom Property Editors**: UI for custom data types
- **Custom List Editors**: Alternative list representations
- **Custom Templates**: Application shell customization
- **Custom Actions**: New user commands
- **Custom View Items**: Embed custom UI in Views

### 38.2 Integration
- **Non-XAF Applications**: Use XAF data in external apps
- **External Data Sources**: Connect to external systems
- **Third-Party Libraries**: Integrate NuGet packages
- **Legacy Forms**: Show existing WinForms in XAF

---

## 39. Error Handling & Troubleshooting

### 39.1 Error Handling
- **Exception Handling**: Catch and handle errors
- **User-Friendly Messages**: Display meaningful errors
- **Error Logging**: Log errors for diagnostics
- **Validation Errors**: Display validation messages
- **Blazor Error Boundary**: Global error handling (Blazor)

### 39.2 Troubleshooting
- **FAQ**: Frequently Asked Questions
- **Common Issues**: Known problems and solutions
- **Debugging Guides**: Step-by-step troubleshooting
- **Log Analysis**: Interpret log files
- **Support Resources**: Access DevExpress support

---

## 40. Technical Terminology

### 40.1 XAF-Specific Terms
- **XAF Application**: Application built with eXpressApp Framework
- **XAF Module**: Pluggable functional component
- **Business Object**: Data entity (synonymous with Business Class)
- **Persistent Object**: Database-mapped object
- **Detail Form**: Alternative name for Detail View
- **List Form**: Alternative name for List View
- **Property**: Object field or property
- **Member**: Business class property or field
- **Caption**: Display label for UI elements
- **Display Name**: Human-readable name

### 40.2 General Terms
- **CRUD**: Create, Read, Update, Delete operations
- **ORM**: Object-Relational Mapping
- **LINQ**: Language Integrated Query
- **MVC**: Model-View-Controller pattern
- **DI**: Dependency Injection
- **SaaS**: Software as a Service
- **REST**: Representational State Transfer
- **API**: Application Programming Interface
- **JWT**: JSON Web Token
- **OAuth2**: Open Authorization standard
- **DBMS**: Database Management System

---

## 41. Component Categories (from Support Ticket Classification)

The following categories represent common areas where users seek support and guidance:

1. **High DPI / 4K / DPI-aware**: High-resolution display support
2. **WinForms UI Platform Specifics**: Windows Forms-specific features
3. **.NET API**: .NET-specific functionality
4. **AI**: Artificial intelligence features
5. **Application Model**: Metadata and UI configuration
6. **Audit Trail Module**: Change tracking
7. **Business / Data Module Design**: Data model architecture
8. **Chart Module**: Data visualization
9. **Clone Module**: Object duplication
10. **Code Analysis (Roslyn Analyzers)**: Automatic error detection
11. **Conditional Appearance Module**: Dynamic UI styling
12. **Controllers**: Logic containers
13. **Actions**: Menu commands and buttons
14. **Frame/Form Templates**: Application shell design
15. **Dashboards Module**: Multi-view analytics
16. **Data Locking / Concurrency Control**: Optimistic/pessimistic locking
17. **Data Manipulation and Business Logic**: CRUD and business rules
18. **Data Representation, Sources, and Modes**: Views and data access
19. **Data Store Configuration**: Database connection setup
20. **Debugging, Testing and Error Handling**: Quality assurance
21. **Deployment**: Application distribution
22. **File Attachment Module**: Document management
23. **Filtering and Querying Data**: Data retrieval
24. **Frameworks**: Core infrastructure (EF Core, XPO)
25. **Images**: Icon and image management
26. **Localization / Accessibility**: Multi-language and accessibility
27. **Multi-Tenancy (SaaS-ready/multiple tenants)**: Multi-tenant architecture
28. **Navigation System**: Application navigation
29. **Notification Module**: Reminders and alerts
30. **Office Module (Rich Text and Spreadsheet)**: Document editing
31. **Performance**: Optimization and scalability
32. **Pivot Grid Module**: OLAP analysis
33. **Pivot Chart (Analysis) Module**: Combined pivot and charts
34. **Reports Module**: Report generation and printing
35. **Scheduler Module**: Calendar and appointments
36. **Security Module**: Authentication and authorization
37. **Solution Structure and Module Design**: Application architecture
38. **State Machine Module**: State transition management
39. **TreeList Editor Module**: Hierarchical data display
40. **Validation Module**: Data validation
41. **View Variants Module**: Alternative View layouts
42. **Views**: List, Detail, and Dashboard Views
43. **View Items**: Elements within Views
44. **Property Editors**: UI controls for properties

---

## Summary

This document provides a comprehensive taxonomy of XAF concepts organized into 41 major categories with detailed subcategories. These concepts cover:

- **Core architecture** (MVC, modules, application model)
- **Data layer** (ORM, business classes, relationships)
- **UI construction** (views, property editors, templates)
- **Business logic** (controllers, actions, validation)
- **Security** (authentication, authorization, permissions)
- **Specialized modules** (reports, dashboards, scheduler, audit trail, etc.)
- **Advanced features** (DI, multi-tenancy, Web API)
- **Platform specifics** (Blazor, WinForms)
- **Development practices** (testing, debugging, deployment, performance)

This taxonomy can be used to:
1. Train semantic models to understand XAF documentation
2. Categorize and tag documentation articles
3. Route support tickets to appropriate teams
4. Build knowledge bases and search indices
5. Generate context-aware help and suggestions
6. Improve documentation navigation and discovery

---

**Last Updated**: February 9, 2026  
**XAF Version**: 25.2  
**Document Version**: 1.0
