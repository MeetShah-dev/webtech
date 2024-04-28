import { HttpService } from '@nestjs/axios';
import { Injectable } from '@nestjs/common';
import { firstValueFrom } from 'rxjs';
import axios from "axios"
const BLOGGING_API = process.env.BLOGGING_API
const NOTIFICATION_API = process.env.NOTIFICATION_API
@Injectable()
export class BlogService {
    constructor(
        private httpService: HttpService
    ) { }
    async createBlog(req, res) {
        let payload = req.body;
        payload = { ...payload, "user": req.user.id.toString() }
        console.log("USER--", typeof (payload))
        try {
            const response = await firstValueFrom(this.httpService.post(BLOGGING_API + 'create-blog/', payload, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async getLatestMagazine(req, res) {
        const response = await firstValueFrom(this.httpService.get(BLOGGING_API + 'magazine-feed/'));
        return res.json(response.data);
    }
    async getArchiveMagazine(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'archived-magazine/', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getUserReadBlog(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-user-blogs/', {
                data: req.body
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getUserDrafts(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-drafts/', {
                data: {
                    user: req.user.id.toString()
                }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getReadBlog(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-blog/', {

                data: {
                    ...req.body,
                    user: req.user.id.toString()
                },
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async updateBlog(req, res) {
        let payload = req.body;
        payload = { ...payload, "user": req.user.id.toString() }
        try {
            const response = await firstValueFrom(this.httpService.put(BLOGGING_API + 'update-blog/', payload, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async deleteBlog(req, res) {
        try {
            const response: any = await axios.delete(BLOGGING_API + 'delete-blog/', {
                data: { ...req.body, "user": req.user.id.toString() }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async deleteFile(req, res) {
        try {
            const response: any = await axios.delete(BLOGGING_API + 'delete-file/', {
                data: { ...req.body, "user": req.user.toString() }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async getReadUserRejectedBlogs(req, res) {
        try {
            const response: any = await axios.get(BLOGGING_API + 'read-user-rejected-blogs/', {
                data: { "user": req.user.id.toString() }
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
    async addReader(req, res) {
        let payload = req.body;
        payload = { ...payload, "user": req.user.id.toString() }
        try {
            const response = await firstValueFrom(this.httpService.post(BLOGGING_API + 'add-reader/', payload, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }));
            return res.json(response.data);
        } catch (e) {
            console.log("error", e)
        }
    }
    async getUserNotifications(req, res) {
        try {
            const response: any = await axios.get(NOTIFICATION_API + 'user-notifications/', {
                data: { "user": req.user.id.toString()}
            })
            return res.json(response.data);
        } catch (e) {
            console.log(e)
        }
    }
}
