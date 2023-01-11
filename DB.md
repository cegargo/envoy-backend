# Database

## Tables

### Student

| Key | Fields          | Data Type |
| --- | --------------- | --------- |
| Pk  | StudentID       | Integer   |
|     | StudentName     | String    |
|     | CourseEnrolled  | String    |
|     | StudentEmail    | String    |
|     | StudentPassword | String    |
|     | DataRegistered  | DateTime  |

### Faculty

| Key | Fields             | Data Type |
| --- | ------------------ | --------- |
| Pk  | FacultyID          | Integer   |
|     | FacultyName        | String    |
|     | CourseAdministered | String    |
|     | FacultyEmail       | String    |
|     | FacultyPassword    | String    |
|     | DataRegistered     | DateTime  |

### Announcement

| Key | Fields           | Data Type |
| --- | ---------------- | --------- |
| Pk  | AnnouncementID   | Integer   |
|     | PostedDateTime   | DateTime  |
|     | AnnouncementType | String    |
|     | Author           | String    |
|     | NumberOfViews    | Integer   |
|     | Duration         | Time      |

### AnnouncementContent

| Key | Fields                | Data Type |
| --- | --------------------- | --------- |
| Pk  | AnnouncementContentID | Integer   |
| Fk  | AnnouncementID        | Integer   |
|     | Description           | String    |
|     | Image                 | URL       |
|     | URL                   | URL       |
