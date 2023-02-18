select GLUCOSE,bloodpressure from {{ source('public', 'diabetes') }}
