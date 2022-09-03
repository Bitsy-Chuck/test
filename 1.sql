create database tyube;

create table video
(id serial not null,
url text not null,
local_path text not null,
is_downloaded bool not null default false,
is_merged bool not null default false,
last_merged_at timestamp,
category text not null,
subcategory text not null,
duration bigint,
title text not null,
description text,
is_short bool not null default true,
constraint pk_video_id primary key(id),
constraint uq_video_url unique(url));
